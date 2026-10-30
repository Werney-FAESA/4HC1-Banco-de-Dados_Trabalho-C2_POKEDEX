from __future__ import annotations

from typing import Optional

from conexion.conexion import PostgresQueries
from model.regiao import Regiao
from utils.exclusao_segura import excluir_registro_seguro


class Controller_Regiao:
    TABLE_NAME = "tb_regiao"

    def inserir_regiao(self) -> Optional[Regiao]:
        """Solicita os dados e insere uma região no banco."""
        postgres = PostgresQueries(can_write=True)
        self.listar_regioes(postgres)

        try:
            id_regiao = int(input("\nDigite o ID para a nova região: "))
        except ValueError:
            print("[ERRO] O ID deve ser um número inteiro.")
            return None

        if self.verifica_existencia(postgres, id_regiao):
            print(f"\n[AVISO] O ID {id_regiao} já existe.")
            return None

        nome_regiao = input("Digite o nome da região: ").strip()
        if not nome_regiao:
            print("[ERRO] O nome da região não pode ficar vazio.")
            return None

        professor = input(
            "Digite o professor responsável (opcional): "
        ).strip() or None

        postgres.write(
            f"""
            INSERT INTO {self.TABLE_NAME}
                (id_regiao, nome_regiao, professor_responsavel)
            VALUES (%s, %s, %s)
            """,
            (id_regiao, nome_regiao, professor),
        )

        nova_regiao = self._buscar_regiao(postgres, id_regiao)
        if nova_regiao is None:
            print("[ERRO] A região foi inserida, mas não pôde ser recuperada.")
            return None

        print("\n[SUCESSO] Região inserida com sucesso:")
        print(nova_regiao.to_string())
        return nova_regiao

    def adicionar_regiao(self) -> Optional[Regiao]:
        """Mantém compatibilidade com chamadas antigas."""
        return self.inserir_regiao()

    def atualizar_regiao(self) -> Optional[Regiao]:
        """Lista as regiões, solicita o ID e atualiza os dados."""
        postgres = PostgresQueries(can_write=True)
        self.listar_regioes(postgres)

        try:
            id_regiao = int(input("\nDigite o ID da região para alterar: "))
        except ValueError:
            print("[ERRO] O ID deve ser um número inteiro.")
            return None

        if not self.verifica_existencia(postgres, id_regiao):
            print(f"\n[AVISO] A região {id_regiao} não existe.")
            return None

        novo_nome = input("Digite o novo nome da região: ").strip()
        if not novo_nome:
            print("[ERRO] O nome da região não pode ficar vazio.")
            return None

        novo_professor = input(
            "Digite o novo professor responsável (opcional): "
        ).strip() or None

        postgres.write(
            f"""
            UPDATE {self.TABLE_NAME}
            SET nome_regiao = %s, professor_responsavel = %s
            WHERE id_regiao = %s
            """,
            (novo_nome, novo_professor, id_regiao),
        )

        regiao_atualizada = self._buscar_regiao(postgres, id_regiao)
        if regiao_atualizada is None:
            print("[ERRO] A região foi atualizada, mas não pôde ser recuperada.")
            return None

        print("\n[SUCESSO] Região atualizada com sucesso:")
        print(regiao_atualizada.to_string())
        return regiao_atualizada

    def excluir_regiao(self) -> bool:
        """Exclui uma região utilizando o padrão de exclusão segura (trava de FK)."""
        postgres = PostgresQueries(can_write=True)
        self.listar_regioes(postgres)

        try:
            id_regiao = int(input("\nDigite o ID da região para excluir: "))
        except ValueError:
            print("[ERRO] O ID deve ser um número inteiro.")
            return False

        if not self.verifica_existencia(postgres, id_regiao):
            print(f"\n[AVISO] A região {id_regiao} não existe.")
            return False

        regiao = self._buscar_regiao(postgres, id_regiao)
        nome = regiao.get_nome_regiao() if regiao else id_regiao
        return excluir_registro_seguro("tb_regiao", id_regiao, f"a região {nome}")

    def verifica_existencia(
        self, postgres: PostgresQueries, id_regiao: int
    ) -> bool:
        """Retorna True quando a região existe no banco."""
        df_regiao = postgres.sqlToDataFrame(
            f"SELECT 1 FROM {self.TABLE_NAME} WHERE id_regiao = %s",
            (id_regiao,),
        )
        return not df_regiao.empty

    def verifica_existencia_regiao(
        self, postgres: PostgresQueries, id_regiao: int
    ) -> bool:
        """Mantém compatibilidade com chamadas antigas do controller."""
        return self.verifica_existencia(postgres, id_regiao)

    def verifica_regiao(
        self, postgres: PostgresQueries, id_regiao: int
    ) -> bool:
        """Mantém compatibilidade com chamadas antigas do controller."""
        return self.verifica_existencia(postgres, id_regiao)

    def verifica_vinculo_fk(
        self, postgres: PostgresQueries, id_regiao: int
    ) -> bool:
        """Verifica se há Pokémon ou treinadores vinculados à região."""
        df_vinculos = postgres.sqlToDataFrame(
            """
            SELECT EXISTS (
                SELECT 1
                FROM tb_pokemon
                WHERE id_regiao = %s
            ) OR EXISTS (
                SELECT 1
                FROM tb_treinador
                WHERE id_regiao = %s
            ) AS possui_vinculos
            """,
            (id_regiao, id_regiao),
        )
        return bool(df_vinculos.iloc[0]["possui_vinculos"])

    def listar_regioes(
        self, postgres: Optional[PostgresQueries] = None
    ) -> None:
        """Lista todas as regiões cadastradas no console."""
        conexao = postgres or PostgresQueries()
        df_regioes = conexao.sqlToDataFrame(
            f"""
            SELECT id_regiao, nome_regiao, professor_responsavel
            FROM {self.TABLE_NAME}
            ORDER BY id_regiao
            """
        )

        print("\n--- REGIÕES CADASTRADAS ---")
        if df_regioes.empty:
            print("Nenhuma região cadastrada até o momento.")
        else:
            print(df_regioes.to_string(index=False))
        print("---------------------------")

    def _buscar_regiao(
        self, postgres: PostgresQueries, id_regiao: int
    ) -> Optional[Regiao]:
        df_regiao = postgres.sqlToDataFrame(
            f"""
            SELECT id_regiao, nome_regiao, professor_responsavel
            FROM {self.TABLE_NAME}
            WHERE id_regiao = %s
            """,
            (id_regiao,),
        )
        if df_regiao.empty:
            return None

        registro = df_regiao.iloc[0]
        professor = registro["professor_responsavel"]
        return Regiao(
            id_regiao=int(registro["id_regiao"]),
            nome_regiao=str(registro["nome_regiao"]),
            professor_responsavel=None if professor is None else str(professor),
        )
