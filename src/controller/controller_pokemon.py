"""Operações CRUD da entidade ``TB_POKEMON``.

O módulo mantém as consultas SQL explícitas e usa parâmetros do psycopg2 para
que valores informados no console não sejam interpretados como SQL.
"""

from __future__ import annotations

from typing import Optional

from psycopg2 import DatabaseError, IntegrityError

from conexion.conexion import PostgresQueries
from model.pokemon import Pokemon


class Controller_Pokemon:
    """Controla a inclusão, consulta, alteração e exclusão de Pokémons."""

    QUERY_LISTAR = """
        SELECT p.id_pokemon, p.nome_pokemon, p.tipo_primario,
               p.tipo_secundario, p.nivel_base, p.id_regiao,
               r.nome_regiao
          FROM tb_pokemon p
          JOIN tb_regiao r ON r.id_regiao = p.id_regiao
         ORDER BY p.id_pokemon
    """
    QUERY_LISTAR_REGIOES = """
        SELECT id_regiao, nome_regiao, professor_responsavel
          FROM tb_regiao
         ORDER BY id_regiao
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

    @staticmethod
    def _confirmar(mensagem: str) -> bool:
        return input(mensagem).strip().upper() in {"S", "SIM"}

    def listar_pokemons(self) -> bool:
        """Lista os Pokémons e sua região; retorna se havia registros."""
        return self._mostrar_tabela(
            self._consultar(self.QUERY_LISTAR),
            "Nenhum Pokémon cadastrado.",
        )

    def listar_regioes(self) -> bool:
        """Lista as regiões disponíveis para associação com um Pokémon."""
        return self._mostrar_tabela(
            self._consultar(self.QUERY_LISTAR_REGIOES),
            "Nenhuma região cadastrada. Cadastre uma região antes de inserir Pokémon.",
        )

    def verifica_existencia(self, id_pokemon: int) -> bool:
        """Informa se o identificador de Pokémon já está cadastrado."""
        resultado = self._consultar(
            "SELECT 1 FROM tb_pokemon WHERE id_pokemon = %s",
            (id_pokemon,),
        )
        return not resultado.empty

    def _regiao_existe(self, id_regiao: int) -> bool:
        resultado = self._consultar(
            "SELECT 1 FROM tb_regiao WHERE id_regiao = %s",
            (id_regiao,),
        )
        return not resultado.empty

    def _buscar_pokemon(self, id_pokemon: int):
        resultado = self._consultar(
            """
            SELECT p.id_pokemon, p.nome_pokemon, p.tipo_primario,
                   p.tipo_secundario, p.nivel_base, p.id_regiao,
                   r.nome_regiao
              FROM tb_pokemon p
              JOIN tb_regiao r ON r.id_regiao = p.id_regiao
             WHERE p.id_pokemon = %s
            """,
            (id_pokemon,),
        )
        return None if resultado.empty else resultado.iloc[0]

    def _montar_pokemon(self, id_pokemon: int) -> Optional[Pokemon]:
        """Cria o objeto de domínio a partir do registro recém-gravado."""
        registro = self._buscar_pokemon(id_pokemon)
        if registro is None:
            return None
        return Pokemon(
            id_pokemon=int(registro["id_pokemon"]),
            nome_pokemon=registro["nome_pokemon"],
            tipo_primario=registro["tipo_primario"],
            tipo_secundario=registro["tipo_secundario"],
            nivel_base=registro["nivel_base"],
        )

    def inserir_pokemon(self) -> Optional[Pokemon]:
        """Coleta os dados no console e inclui um Pokémon associado a uma região."""
        print("\n--- Inserir Pokémon ---")
        id_pokemon = self._ler_inteiro("ID do Pokémon: ", minimo=1)
        if self.verifica_existencia(id_pokemon):
            print("Já existe um Pokémon cadastrado com este ID.")
            return None

        if not self.listar_regioes():
            return None
        id_regiao = self._ler_inteiro("ID da região de origem: ", minimo=1)
        if not self._regiao_existe(id_regiao):
            print("A região informada não existe.")
            return None

        nome_pokemon = self._ler_texto("Nome: ")
        tipo_primario = self._ler_texto("Tipo primário: ")
        tipo_secundario = self._ler_texto("Tipo secundário (opcional): ", obrigatorio=False)
        nivel_base = self._ler_inteiro("Nível base: ", minimo=0)

        try:
            PostgresQueries(can_write=True).write(
                """
                INSERT INTO tb_pokemon
                    (id_pokemon, nome_pokemon, tipo_primario, tipo_secundario, nivel_base, id_regiao)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (id_pokemon, nome_pokemon, tipo_primario, tipo_secundario, nivel_base, id_regiao),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível inserir o Pokémon: {erro}")
            return None

        pokemon = self._montar_pokemon(id_pokemon)
        print("Pokémon inserido com sucesso.")
        if pokemon:
            print(pokemon.to_string())
        return pokemon

    def atualizar_pokemon(self) -> Optional[Pokemon]:
        """Atualiza os atributos atômicos e a região de um Pokémon existente."""
        print("\n--- Atualizar Pokémon ---")
        if not self.listar_pokemons():
            return None
        id_pokemon = self._ler_inteiro("ID do Pokémon a atualizar: ", minimo=1)
        atual = self._buscar_pokemon(id_pokemon)
        if atual is None:
            print("Pokémon não encontrado.")
            return None

        nome_pokemon = self._ler_texto(f"Nome [{atual['nome_pokemon']}]: ", obrigatorio=False) or atual["nome_pokemon"]
        tipo_primario = self._ler_texto(f"Tipo primário [{atual['tipo_primario']}]: ", obrigatorio=False) or atual["tipo_primario"]
        tipo_secundario_atual = atual["tipo_secundario"] or "sem tipo secundário"
        tipo_secundario = self._ler_texto(
            f"Tipo secundário [{tipo_secundario_atual}] (vazio mantém): ",
            obrigatorio=False,
        )
        if tipo_secundario is None:
            tipo_secundario = atual["tipo_secundario"]

        nivel_texto = input(f"Nível base [{atual['nivel_base']}]: ").strip()
        if nivel_texto:
            try:
                nivel_base = int(nivel_texto)
                if nivel_base < 0:
                    raise ValueError
            except ValueError:
                print("Nível base inválido.")
                return None
        else:
            nivel_base = atual["nivel_base"]

        if not self.listar_regioes():
            return None
        regiao_texto = input(f"ID da região [{atual['id_regiao']}]: ").strip()
        if regiao_texto:
            try:
                id_regiao = int(regiao_texto)
            except ValueError:
                print("ID da região inválido.")
                return None
            if not self._regiao_existe(id_regiao):
                print("A região informada não existe.")
                return None
        else:
            id_regiao = int(atual["id_regiao"])

        try:
            PostgresQueries(can_write=True).write(
                """
                UPDATE tb_pokemon
                   SET nome_pokemon = %s,
                       tipo_primario = %s,
                       tipo_secundario = %s,
                       nivel_base = %s,
                       id_regiao = %s
                 WHERE id_pokemon = %s
                """,
                (nome_pokemon, tipo_primario, tipo_secundario, nivel_base, id_regiao, id_pokemon),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível atualizar o Pokémon: {erro}")
            return None

        pokemon = self._montar_pokemon(id_pokemon)
        print("Pokémon atualizado com sucesso.")
        if pokemon:
            print(pokemon.to_string())
        return pokemon

    def excluir_pokemon(self) -> bool:
        """Exclui um Pokémon somente quando ele não possui evoluções dependentes."""
        print("\n--- Excluir Pokémon ---")
        if not self.listar_pokemons():
            return False
        id_pokemon = self._ler_inteiro("ID do Pokémon a excluir: ", minimo=1)
        if not self.verifica_existencia(id_pokemon):
            print("Pokémon não encontrado.")
            return False

        dependencias = self._consultar(
            """
            SELECT EXISTS (
                SELECT 1
                  FROM tb_evolucao
                 WHERE id_pokemon_base = %s OR id_pokemon_evoluido = %s
            ) AS possui_dependencias
            """,
            (id_pokemon, id_pokemon),
        )
        if not dependencias.empty and bool(dependencias.iloc[0]["possui_dependencias"]):
            print("Não é possível excluir o registro pois ele possui registros dependentes em outra tabela.")
            return False

        if not self._confirmar("Confirma a exclusão deste Pokémon? (S/N): "):
            print("Exclusão cancelada.")
            return False

        try:
            PostgresQueries(can_write=True).write(
                "DELETE FROM tb_pokemon WHERE id_pokemon = %s",
                (id_pokemon,),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível excluir o Pokémon: {erro}")
            return False

        print("Pokémon excluído com sucesso.")
        return True
