from __future__ import annotations

from typing import Optional

from psycopg2 import DatabaseError, IntegrityError

from conexion.conexion import PostgresQueries
from model.regiao import Regiao
from model.treinador import Treinador
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Treinador:
    TABLE_NAME = "tb_treinador"

    QUERY_LISTAR = """
        SELECT t.id_treinador, t.nome, t.idade, t.id_regiao,
               r.nome_regiao
          FROM tb_treinador t
          JOIN tb_regiao r ON r.id_regiao = t.id_regiao
         ORDER BY t.id_treinador
    """

    def _consultar(self, query: str, params=None):
        return PostgresQueries().sqlToDataFrame(query, params)

    @staticmethod
    def _mostrar_tabela(tabela, mensagem_vazia: str) -> bool:
        if tabela.empty:
            print(mensagem_vazia)
            return False
        print(tabela.to_string(index=False))
        return True

    @staticmethod
    def _ler_inteiro(
        mensagem: str,
        minimo: Optional[int] = None,
        maximo: Optional[int] = None,
        padrao: Optional[int] = None,
    ) -> int:
        while True:
            texto = input(mensagem).strip()
            if not texto and padrao is not None:
                return padrao
            try:
                valor = int(texto)
            except ValueError:
                print("Informe um número inteiro válido.")
                continue
            if minimo is not None and valor < minimo:
                print(f"Informe um número maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Informe um número menor ou igual a {maximo}.")
                continue
            return valor

    @staticmethod
    def _ler_texto(mensagem: str, obrigatorio: bool = True) -> Optional[str]:
        while True:
            valor = input(mensagem).strip()
            if valor or not obrigatorio:
                return valor or None
            print("Este campo é obrigatório.")

    def listar_treinadores(
        self, postgres: Optional[PostgresQueries] = None
    ) -> None:
        conexao = postgres or PostgresQueries()
        df_treinadores = conexao.sqlToDataFrame(self.QUERY_LISTAR)

        print("\n--- TREINADORES CADASTRADOS ---")
        if df_treinadores.empty:
            print("Nenhum treinador cadastrado até o momento.")
        else:
            print(df_treinadores.to_string(index=False))
        print("-------------------------------")

    def listar_treinador(
        self, postgres: Optional[PostgresQueries] = None
    ) -> None:
        """Mantém compatibilidade com chamadas antigas."""
        self.listar_treinadores(postgres)

    def listar_regioes(self) -> bool:
        return self._mostrar_tabela(
            self._consultar(self.QUERY_LISTAR_REGIOES),
            "Nenhuma região cadastrada. Cadastre uma região antes de inserir treinadores.",
        )

    def verifica_existencia(
        self, postgres: Optional[PostgresQueries], id_treinador: int
    ) -> bool:
        conexao = postgres or PostgresQueries()
        resultado = conexao.sqlToDataFrame(
            f"SELECT 1 FROM {self.TABLE_NAME} WHERE id_treinador = %s",
            (id_treinador,),
        )
        return not resultado.empty

    def verifica_existencia_treinador(
        self, postgres: Optional[PostgresQueries], id_treinador: int
    ) -> bool:
        return self.verifica_existencia(postgres, id_treinador)

    def verifica_treinador(
        self, postgres: Optional[PostgresQueries], id_treinador: int
    ) -> bool:
        return self.verifica_existencia(postgres, id_treinador)

    def _regiao_existe(self, id_regiao: int) -> bool:
        resultado = self._consultar(
            "SELECT 1 FROM tb_regiao WHERE id_regiao = %s",
            (id_regiao,),
        )
        return not resultado.empty

    def verifica_vinculo_fk(
        self, postgres: PostgresQueries, id_treinador: int
    ) -> bool:
        df_vinculos = postgres.sqlToDataFrame(
            """
            SELECT EXISTS (
                SELECT 1
                  FROM tb_batalha
                 WHERE id_treinador_1 = %s
                    OR id_treinador_2 = %s
                    OR id_vencedor = %s
            ) AS possui_vinculos
            """,
            (id_treinador, id_treinador, id_treinador),
        )
        return bool(df_vinculos.iloc[0]["possui_vinculos"])

    def _buscar_treinador(
        self, postgres: PostgresQueries, id_treinador: int
    ) -> Optional[Treinador]:
        resultado = postgres.sqlToDataFrame(
            """
            SELECT t.id_treinador, t.nome, t.idade, t.id_regiao,
                   r.nome_regiao, r.professor_responsavel
              FROM tb_treinador t
              JOIN tb_regiao r ON r.id_regiao = t.id_regiao
             WHERE t.id_treinador = %s
            """,
            (id_treinador,),
        )
        if resultado.empty:
            return None

        registro = resultado.iloc[0]
        idade = registro["idade"]
        regiao = Regiao(
            id_regiao=int(registro["id_regiao"]),
            nome_regiao=str(registro["nome_regiao"]),
            professor_responsavel=(
                None
                if registro["professor_responsavel"] is None
                else str(registro["professor_responsavel"])
            ),
        )
        return Treinador(
            id_treinador=int(registro["id_treinador"]),
            nome_treinador=str(registro["nome"]),
            regiao=regiao,
            idade=None if idade is None else int(idade),
        )

    def inserir_treinador(self) -> Optional[Treinador]:
        print("\n--- Inserir Treinador ---")
        id_treinador = self._ler_inteiro("ID do treinador: ", minimo=1)
        if self.verifica_existencia(PostgresQueries(), id_treinador):
            print("Já existe um treinador cadastrado com este ID.")
            return None

        if not self.listar_regioes():
            return None
        id_regiao = self._ler_inteiro("ID da região: ", minimo=1)
        if not self._regiao_existe(id_regiao):
            print("A região informada não existe.")
            return None

        nome_treinador = self._ler_texto("Nome: ")
        idade_texto = input("Idade (opcional): ").strip()
        idade = None
        if idade_texto:
            try:
                idade = int(idade_texto)
                if idade < 0 or idade > 150:
                    print("A idade deve estar entre 0 e 150.")
                    return None
            except ValueError:
                print("A idade informada não é um número inteiro válido.")
                return None

        try:
            PostgresQueries(can_write=True).write(
                """
                INSERT INTO tb_treinador (id_treinador, nome, idade, id_regiao)
                VALUES (%s, %s, %s, %s)
                """,
                (id_treinador, nome_treinador, idade, id_regiao),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível inserir o treinador: {erro}")
            return None

        novo_treinador = self._buscar_treinador(
            PostgresQueries(), id_treinador
        )
        print("Treinador inserido com sucesso.")
        if novo_treinador:
            print(novo_treinador.to_string())
        return novo_treinador

    def adicionar_treinador(self) -> Optional[Treinador]:
        return self.inserir_treinador()

    def atualizar_treinador(self) -> Optional[Treinador]:
        print("\n--- Atualizar Treinador ---")
        if not self._mostrar_tabela(
            self._consultar(self.QUERY_LISTAR),
            "Nenhum treinador cadastrado.",
        ):
            return None

        id_treinador = self._ler_inteiro("ID do treinador a atualizar: ", minimo=1)
        postgres = PostgresQueries()
        atual = self._buscar_treinador(postgres, id_treinador)
        if atual is None:
            print("Treinador não encontrado.")
            return None

        nome_treinador = (
            self._ler_texto(
                f"Nome [{atual.get_nome_treinador()}]: ",
                obrigatorio=False,
            )
            or atual.get_nome_treinador()
        )

        idade_texto = input(
            f"Idade [{atual.get_idade() if atual.get_idade() is not None else 'sem idade'}] "
            "(vazio mantém): "
        ).strip()
        idade = atual.get_idade()
        if idade_texto:
            try:
                idade = int(idade_texto)
                if idade < 0 or idade > 150:
                    print("A idade deve estar entre 0 e 150.")
                    return None
            except ValueError:
                print("A idade informada não é um número inteiro válido.")
                return None

        if not self.listar_regioes():
            return None
        regiao_atual = atual.get_regiao()
        id_regiao_atual = regiao_atual.get_id_regiao() if regiao_atual else None
        regiao_texto = input(
            f"ID da região [{id_regiao_atual}]: "
        ).strip()
        if regiao_texto:
            try:
                id_regiao = int(regiao_texto)
            except ValueError:
                print("ID da região inválido.")
                return None
        else:
            id_regiao = id_regiao_atual

        if id_regiao is None or not self._regiao_existe(id_regiao):
            print("A região informada não existe.")
            return None

        try:
            PostgresQueries(can_write=True).write(
                """
                UPDATE tb_treinador
                   SET nome = %s, idade = %s, id_regiao = %s
                 WHERE id_treinador = %s
                """,
                (nome_treinador, idade, id_regiao, id_treinador),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível atualizar o treinador: {erro}")
            return None

        treinador_atualizado = self._buscar_treinador(
            PostgresQueries(), id_treinador
        )
        print("Treinador atualizado com sucesso.")
        if treinador_atualizado:
            print(treinador_atualizado.to_string())
        return treinador_atualizado

    @staticmethod
    def _confirmar(mensagem: str) -> bool:
        return input(mensagem).strip().upper() in {"S", "SIM"}

    def _contar_batalhas(self, id_treinador: int) -> int:
        """Quantidade de batalhas em que o treinador é desafiante, desafiado ou vencedor."""
        resultado = self._consultar(
            """
            SELECT COUNT(*) AS total
              FROM tb_batalha
             WHERE id_treinador_1 = %s
                OR id_treinador_2 = %s
                OR id_vencedor = %s
            """,
            (id_treinador, id_treinador, id_treinador),
        )
        return 0 if resultado.empty else int(resultado.iloc[0]["total"])

    def excluir_treinador(self) -> bool:
        """Exclui um treinador com trava de chave estrangeira em TB_BATALHA."""
        print("\n--- Excluir Treinador ---")
        if not self._mostrar_tabela(
            self._consultar(self.QUERY_LISTAR),
            "Nenhum treinador cadastrado.",
        ):
            return False

        id_treinador = self._ler_inteiro("ID do treinador a excluir: ", minimo=1)
        if not self.verifica_existencia(PostgresQueries(), id_treinador):
            print("Treinador não encontrado.")
            return False

        treinador = self._buscar_treinador(PostgresQueries(), id_treinador)
        nome = treinador.get_nome_treinador() if treinador else id_treinador

        if self.verifica_vinculo_fk(PostgresQueries(), id_treinador):
            # Trava de FK: o treinador é pai de registros em TB_BATALHA.
            total = self._contar_batalhas(id_treinador)
            print(
                "Não é possível excluir o registro pois ele possui registros "
                "dependentes em outra tabela."
            )
            print(f"O treinador {nome} participa de {total} batalha(s) (TB_BATALHA).")
            if not self._confirmar(
                "Deseja excluir primeiro os registros dependentes vinculados? (S/N): "
            ):
                print("Exclusão cancelada.")
                return False

            # Os dois DELETEs vão na mesma chamada, portanto na mesma transação:
            # se qualquer um falhar, o write() faz rollback e nada é removido.
            query = (
                "DELETE FROM tb_batalha "
                " WHERE id_treinador_1 = %s OR id_treinador_2 = %s OR id_vencedor = %s; "
                "DELETE FROM tb_treinador WHERE id_treinador = %s"
            )
            params = (id_treinador, id_treinador, id_treinador, id_treinador)
        else:
            if not self._confirmar(f"Confirma a exclusão do treinador {nome}? (S/N): "):
                print("Exclusão cancelada.")
                return False
            query = "DELETE FROM tb_treinador WHERE id_treinador = %s"
            params = (id_treinador,)

        try:
            PostgresQueries(can_write=True).write(query, params)
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível excluir o treinador: {erro}")
            return False

        print("Treinador excluído com sucesso.")
        return True
