"""Padrão de exclusão segura (item 6.c.5.i do edital).

Toda controladora deve excluir registros através deste módulo, para que o
comportamento seja o mesmo em todas as entidades:

1. Confirma com o usuário se ele deseja realmente remover o registro;
2. Verifica se o registro é chave estrangeira (FK) em outra tabela;
3. Se houver dependentes, informa quais são e pergunta se o usuário deseja
   excluir primeiro os registros dependentes (tabelas filhas);
4. Executa toda a exclusão dentro de uma única transação: ou tudo é
   removido, ou nada é removido (rollback).

Uso nas controladoras:

    from utils.exclusao_segura import excluir_registro_seguro

    excluir_registro_seguro("tb_regiao", id_regiao, "a região Kanto")

Os nomes de tabelas e colunas vêm apenas do mapa fixo abaixo (nunca do
usuário); os valores informados no console são sempre enviados como
parâmetros da consulta.
"""

from __future__ import annotations

from psycopg2 import DatabaseError

from conexion.conexion import PostgresQueries


# Chave primária de cada tabela do modelo relacional.
CHAVES_PRIMARIAS = {
    "tb_regiao": "id_regiao",
    "tb_treinador": "id_treinador",
    "tb_pokemon": "id_pokemon",
    "tb_evolucao": "id_evolucao",
    "tb_batalha": "id_batalha",
}

# Para cada tabela pai: (tabela filha, [colunas FK que apontam para o pai]).
# Espelha as constraints de sql/create_tables.sql.
DEPENDENCIAS = {
    "tb_regiao": [
        ("tb_pokemon", ["id_regiao"]),
        ("tb_treinador", ["id_regiao"]),
    ],
    "tb_pokemon": [
        ("tb_evolucao", ["id_pokemon_base", "id_pokemon_evoluido"]),
    ],
    "tb_treinador": [
        ("tb_batalha", ["id_treinador_1", "id_treinador_2", "id_vencedor"]),
    ],
    "tb_evolucao": [],
    "tb_batalha": [],
}

NOMES_AMIGAVEIS = {
    "tb_regiao": "Regiões",
    "tb_treinador": "Treinadores",
    "tb_pokemon": "Pokémons",
    "tb_evolucao": "Evoluções",
    "tb_batalha": "Batalhas",
}

MENSAGEM_BLOQUEIO = (
    "Não é possível excluir o registro pois ele possui registros "
    "dependentes em outra tabela."
)


def _validar_tabela(tabela: str) -> str:
    tabela = tabela.lower()
    if tabela not in CHAVES_PRIMARIAS:
        raise ValueError(f"Tabela desconhecida para exclusão segura: {tabela}")
    return tabela


def _condicao_fk(colunas: list[str]) -> str:
    """Monta 'col1 = %s OR col2 = %s ...' para as colunas FK informadas."""
    return " OR ".join(f"{coluna} = %s" for coluna in colunas)


def contar_dependentes(tabela: str, id_registro: int) -> dict[str, int]:
    """Retorna {tabela_filha: quantidade} apenas das filhas com registros."""
    tabela = _validar_tabela(tabela)
    resultado: dict[str, int] = {}
    for tabela_filha, colunas in DEPENDENCIAS[tabela]:
        query = (
            f"SELECT COUNT(1) AS total FROM {tabela_filha} "
            f"WHERE {_condicao_fk(colunas)}"
        )
        df = PostgresQueries().sqlToDataFrame(query, (id_registro,) * len(colunas))
        total = int(df.iloc[0]["total"]) if not df.empty else 0
        if total > 0:
            resultado[tabela_filha] = total
    return resultado


def possui_dependentes(tabela: str, id_registro: int) -> bool:
    return bool(contar_dependentes(tabela, id_registro))


def _excluir_recursivo(cursor, tabela: str, id_registro: int, removidos: dict[str, int]):
    """Remove primeiro os netos/filhos e por último o próprio registro."""
    pk = CHAVES_PRIMARIAS[tabela]
    for tabela_filha, colunas in DEPENDENCIAS[tabela]:
        pk_filha = CHAVES_PRIMARIAS[tabela_filha]
        cursor.execute(
            f"SELECT {pk_filha} FROM {tabela_filha} WHERE {_condicao_fk(colunas)}",
            (id_registro,) * len(colunas),
        )
        for (id_filho,) in cursor.fetchall():
            _excluir_recursivo(cursor, tabela_filha, id_filho, removidos)

    cursor.execute(f"DELETE FROM {tabela} WHERE {pk} = %s", (id_registro,))
    removidos[tabela] = removidos.get(tabela, 0) + cursor.rowcount


def excluir_com_dependentes(tabela: str, id_registro: int) -> dict[str, int]:
    """Exclui o registro e todos os dependentes numa única transação.

    Retorna {tabela: quantidade removida}. Em caso de erro faz rollback e
    relança a exceção.
    """
    tabela = _validar_tabela(tabela)
    banco = PostgresQueries(can_write=True)
    cursor = banco.connect()
    removidos: dict[str, int] = {}
    try:
        _excluir_recursivo(cursor, tabela, id_registro, removidos)
        banco.conn.commit()
        return removidos
    except DatabaseError:
        banco.conn.rollback()
        raise
    finally:
        banco.close()


def _confirmar(mensagem: str) -> bool:
    return input(mensagem).strip().upper() in {"S", "SIM"}


def excluir_registro_seguro(tabela: str, id_registro: int, descricao: str = "o registro") -> bool:
    """Fluxo completo e padronizado de exclusão com trava de FK.

    Retorna True se o registro foi excluído.
    """
    tabela = _validar_tabela(tabela)

    if not _confirmar(f"Deseja realmente excluir {descricao}? (S/N): "):
        print("Exclusão cancelada.")
        return False

    dependentes = contar_dependentes(tabela, id_registro)
    if dependentes:
        print(f"\n{MENSAGEM_BLOQUEIO}")
        print("Registros vinculados encontrados:")
        for tabela_filha, total in dependentes.items():
            print(f"  - {NOMES_AMIGAVEIS.get(tabela_filha, tabela_filha)}: {total}")
        if not _confirmar("Deseja excluir primeiro os registros dependentes vinculados? (S/N): "):
            print("Exclusão cancelada. Nenhum registro foi removido.")
            return False

    try:
        removidos = excluir_com_dependentes(tabela, id_registro)
    except DatabaseError as erro:
        print(f"Não foi possível excluir: {erro}")
        return False

    if not removidos.get(tabela):
        print("Registro não encontrado. Nada foi excluído.")
        return False

    print("Exclusão realizada com sucesso.")
    for tabela_removida, total in removidos.items():
        if tabela_removida != tabela:
            print(f"  - Registros dependentes removidos em {NOMES_AMIGAVEIS.get(tabela_removida, tabela_removida)}: {total}")
    return True
