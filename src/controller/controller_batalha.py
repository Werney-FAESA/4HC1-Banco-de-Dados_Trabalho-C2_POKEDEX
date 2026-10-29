"""Operações CRUD da entidade ``TB_BATALHA``.

O módulo mantém as consultas SQL explícitas e usa parâmetros do psycopg2 para
que valores informados no console não sejam interpretados como SQL.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional

from psycopg2 import DatabaseError, IntegrityError

from conexion.conexion import PostgresQueries
from model.batalha import Batalha
from model.treinador import Treinador


class Controller_Batalha:
    """Controla a inclusão, consulta, alteração e exclusão de batalhas."""

    FORMATO_DATA = "%d/%m/%Y"

    QUERY_LISTAR = """
        SELECT b.id_batalha,
               b.id_treinador_1, t1.nome AS treinador_1,
               b.id_treinador_2, t2.nome AS treinador_2,
               b.data_batalha,
               b.id_vencedor, v.nome AS vencedor,
               b.local_batalha
          FROM tb_batalha b
          JOIN tb_treinador t1 ON t1.id_treinador = b.id_treinador_1
          JOIN tb_treinador t2 ON t2.id_treinador = b.id_treinador_2
          JOIN tb_treinador v  ON v.id_treinador  = b.id_vencedor
         ORDER BY b.id_batalha
    """
    QUERY_LISTAR_TREINADORES = """
        SELECT t.id_treinador, t.nome, t.idade, r.nome_regiao
          FROM tb_treinador t
          JOIN tb_regiao r ON r.id_regiao = t.id_regiao
         ORDER BY t.id_treinador
    """

    # ------------------------------------------------------------------ #
    # Utilitários de console e consulta
    # ------------------------------------------------------------------ #
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
    def _ler_inteiro(mensagem: str, minimo: Optional[int] = None) -> int:
        while True:
            try:
                valor = int(input(mensagem).strip())
                if minimo is not None and valor < minimo:
                    print(f"Informe um número maior ou igual a {minimo}.")
                    continue
                return valor
            except ValueError:
                print("Informe um número inteiro válido.")

    @staticmethod
    def _ler_texto(mensagem: str, obrigatorio: bool = True) -> Optional[str]:
        while True:
            valor = input(mensagem).strip()
            if valor or not obrigatorio:
                return valor or None
            print("Este campo é obrigatório.")

    @classmethod
    def _ler_data(cls, mensagem: str) -> date:
        while True:
            texto = input(mensagem).strip()
            try:
                return datetime.strptime(texto, cls.FORMATO_DATA).date()
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA (ex.: 25/10/2026).")

    @staticmethod
    def _confirmar(mensagem: str) -> bool:
        return input(mensagem).strip().upper() in {"S", "SIM"}

    # ------------------------------------------------------------------ #
    # Listagens e verificações
    # ------------------------------------------------------------------ #
    def listar_batalhas(self) -> bool:
        """Lista as batalhas com os nomes dos treinadores; retorna se havia registros."""
        return self._mostrar_tabela(
            self._consultar(self.QUERY_LISTAR),
            "Nenhuma batalha cadastrada.",
        )

    def listar_treinadores(self) -> bool:
        """Lista os treinadores disponíveis para participar de uma batalha."""
        return self._mostrar_tabela(
            self._consultar(self.QUERY_LISTAR_TREINADORES),
            "Nenhum treinador cadastrado. Cadastre treinadores antes de registrar uma batalha.",
        )

    def verifica_existencia(self, id_batalha: int) -> bool:
        """Informa se o identificador de batalha já está cadastrado."""
        resultado = self._consultar(
            "SELECT 1 FROM tb_batalha WHERE id_batalha = %s",
            (id_batalha,),
        )
        return not resultado.empty

    def _treinador_existe(self, id_treinador: int) -> bool:
        resultado = self._consultar(
            "SELECT 1 FROM tb_treinador WHERE id_treinador = %s",
            (id_treinador,),
        )
        return not resultado.empty

    def _buscar_batalha(self, id_batalha: int):
        resultado = self._consultar(
            self.QUERY_LISTAR.replace(
                "ORDER BY b.id_batalha", "WHERE b.id_batalha = %s"
            ),
            (id_batalha,),
        )
        return None if resultado.empty else resultado.iloc[0]

    def _montar_batalha(self, id_batalha: int) -> Optional[Batalha]:
        """Cria o objeto de domínio, com as instâncias de Treinador, a partir do banco."""
        registro = self._buscar_batalha(id_batalha)
        if registro is None:
            return None
        return Batalha(
            id_batalha=int(registro["id_batalha"]),
            treinador_1=Treinador(int(registro["id_treinador_1"]), registro["treinador_1"]),
            treinador_2=Treinador(int(registro["id_treinador_2"]), registro["treinador_2"]),
            data_batalha=registro["data_batalha"],
            vencedor=Treinador(int(registro["id_vencedor"]), registro["vencedor"]),
            local_batalha=registro["local_batalha"],
        )

    # ------------------------------------------------------------------ #
    # CRUD
    # ------------------------------------------------------------------ #
    def inserir_batalha(self) -> Optional[Batalha]:
        """Coleta os dados no console e registra uma batalha entre dois treinadores."""
        print("\n--- Inserir Batalha ---")
        id_batalha = self._ler_inteiro("ID da batalha: ", minimo=1)
        if self.verifica_existencia(id_batalha):
            print("Já existe uma batalha cadastrada com este ID.")
            return None

        if not self.listar_treinadores():
            return None

        id_treinador_1 = self._ler_inteiro("ID do treinador 1 (desafiante): ", minimo=1)
        if not self._treinador_existe(id_treinador_1):
            print("O treinador 1 informado não existe.")
            return None

        id_treinador_2 = self._ler_inteiro("ID do treinador 2 (desafiado): ", minimo=1)
        if id_treinador_2 == id_treinador_1:
            print("Um treinador não pode batalhar contra si mesmo.")
            return None
        if not self._treinador_existe(id_treinador_2):
            print("O treinador 2 informado não existe.")
            return None

        id_vencedor = self._ler_inteiro(
            f"ID do vencedor ({id_treinador_1} ou {id_treinador_2}): ", minimo=1
        )
        if id_vencedor not in (id_treinador_1, id_treinador_2):
            print("O vencedor deve ser um dos dois treinadores da batalha.")
            return None

        data_batalha = self._ler_data(f"Data da batalha ({self.FORMATO_DATA.replace('%d', 'DD').replace('%m', 'MM').replace('%Y', 'AAAA')}): ")
        local_batalha = self._ler_texto("Local da batalha: ")

        try:
            PostgresQueries(can_write=True).write(
                """
                INSERT INTO tb_batalha
                    (id_batalha, id_treinador_1, id_treinador_2,
                     data_batalha, id_vencedor, local_batalha)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (id_batalha, id_treinador_1, id_treinador_2,
                 data_batalha, id_vencedor, local_batalha),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível inserir a batalha: {erro}")
            return None

        batalha = self._montar_batalha(id_batalha)
        print("Batalha inserida com sucesso.")
        if batalha:
            print(batalha.to_string())
        return batalha

    def atualizar_batalha(self) -> Optional[Batalha]:
        """Ajusta local, data ou vencedor de uma batalha existente (antes/depois)."""
        print("\n--- Atualizar Batalha ---")
        if not self.listar_batalhas():
            return None
        id_batalha = self._ler_inteiro("ID da batalha a atualizar: ", minimo=1)
        atual = self._buscar_batalha(id_batalha)
        if atual is None:
            print("Batalha não encontrada.")
            return None

        antes = self._montar_batalha(id_batalha)
        if antes:
            print("\nAntes da atualização:")
            print(antes.to_string())
            print()

        id_t1 = int(atual["id_treinador_1"])
        id_t2 = int(atual["id_treinador_2"])

        local_batalha = (
            self._ler_texto(f"Local [{atual['local_batalha']}]: ", obrigatorio=False)
            or atual["local_batalha"]
        )

        data_atual = atual["data_batalha"]
        data_texto = input(f"Data [{data_atual.strftime(self.FORMATO_DATA)}] (vazio mantém): ").strip()
        if data_texto:
            try:
                data_batalha = datetime.strptime(data_texto, self.FORMATO_DATA).date()
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")
                return None
        else:
            data_batalha = data_atual

        vencedor_texto = input(
            f"ID do vencedor [{atual['id_vencedor']}] ({id_t1} ou {id_t2}): "
        ).strip()
        if vencedor_texto:
            try:
                id_vencedor = int(vencedor_texto)
            except ValueError:
                print("ID do vencedor inválido.")
                return None
            if id_vencedor not in (id_t1, id_t2):
                print("O vencedor deve ser um dos dois treinadores da batalha.")
                return None
        else:
            id_vencedor = int(atual["id_vencedor"])

        try:
            PostgresQueries(can_write=True).write(
                """
                UPDATE tb_batalha
                   SET local_batalha = %s,
                       data_batalha = %s,
                       id_vencedor = %s
                 WHERE id_batalha = %s
                """,
                (local_batalha, data_batalha, id_vencedor, id_batalha),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível atualizar a batalha: {erro}")
            return None

        batalha = self._montar_batalha(id_batalha)
        print("\nBatalha atualizada com sucesso. Depois da atualização:")
        if batalha:
            print(batalha.to_string())
        return batalha

    def excluir_batalha(self) -> bool:
        """Exclui uma batalha após confirmação. Batalha não é pai de nenhuma tabela."""
        print("\n--- Excluir Batalha ---")
        if not self.listar_batalhas():
            return False
        id_batalha = self._ler_inteiro("ID da batalha a excluir: ", minimo=1)
        if not self.verifica_existencia(id_batalha):
            print("Batalha não encontrada.")
            return False

        batalha = self._montar_batalha(id_batalha)
        if batalha:
            print(batalha.to_string())
        if not self._confirmar(f"Confirma a exclusão da batalha {id_batalha}? (S/N): "):
            print("Exclusão cancelada.")
            return False

        try:
            PostgresQueries(can_write=True).write(
                "DELETE FROM tb_batalha WHERE id_batalha = %s",
                (id_batalha,),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível excluir a batalha: {erro}")
            return False

        print("Batalha excluída com sucesso.")
        return True

    # ------------------------------------------------------------------ #
    # Apoio à trava de FK da exclusão de Treinador
    # ------------------------------------------------------------------ #
    def contar_batalhas_do_treinador(self, id_treinador: int) -> int:
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

    def excluir_batalhas_do_treinador(self, id_treinador: int) -> None:
        """Remove todas as batalhas do treinador (usada após confirmação do usuário)."""
        PostgresQueries(can_write=True).write(
            """
            DELETE FROM tb_batalha
             WHERE id_treinador_1 = %s
                OR id_treinador_2 = %s
                OR id_vencedor = %s
            """,
            (id_treinador, id_treinador, id_treinador),
        )
