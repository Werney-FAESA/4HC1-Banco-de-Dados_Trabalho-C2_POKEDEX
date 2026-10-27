"""Operações CRUD da entidade ``TB_EVOLUCAO``.

Uma evolução liga dois Pokémons (base -> evoluído) e guarda como ela
acontece (nível, pedra, troca, amizade...). As duas colunas são chaves
estrangeiras para ``TB_POKEMON``, então antes de gravar sempre é verificado
se os dois Pokémons existem.

As consultas são escritas à mão (sem ORM) e os valores digitados no console
são enviados como parâmetros do psycopg2.
"""

from __future__ import annotations

from typing import Optional

from psycopg2 import DatabaseError, IntegrityError

from conexion.conexion import PostgresQueries
from model.evolucao import Evolucao
from model.pokemon import Pokemon
from utils.exclusao_segura import excluir_registro_seguro


MODOS_EVOLUCAO = [
    "Nível",
    "Pedra do Fogo",
    "Pedra da Água",
    "Pedra do Trovão",
    "Pedra da Folha",
    "Pedra da Lua",
    "Troca",
    "Amizade",
]

NIVEL_MINIMO = 1
NIVEL_MAXIMO = 100


class Controller_Evolucao:
    """Controla a inclusão, consulta, alteração e exclusão de Evoluções."""

    QUERY_LISTAR = """
        SELECT e.id_evolucao,
               e.id_pokemon_base,
               pb.nome_pokemon  AS pokemon_base,
               e.id_pokemon_evoluido,
               pe.nome_pokemon  AS pokemon_evoluido,
               e.nivel_evolucao,
               e.modo_evolucao
          FROM tb_evolucao e
          JOIN tb_pokemon pb ON pb.id_pokemon = e.id_pokemon_base
          JOIN tb_pokemon pe ON pe.id_pokemon = e.id_pokemon_evoluido
    """

    QUERY_LISTAR_POKEMONS = """
        SELECT id_pokemon, nome_pokemon, tipo_primario, tipo_secundario
          FROM tb_pokemon
         ORDER BY id_pokemon
    """

    # ------------------------------------------------------------------
    # Auxiliares de banco e de entrada no console
    # ------------------------------------------------------------------
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
    def _ler_inteiro(mensagem: str, minimo: Optional[int] = None,
                     maximo: Optional[int] = None, padrao: Optional[int] = None) -> int:
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
    def _confirmar(mensagem: str) -> bool:
        return input(mensagem).strip().upper() in {"S", "SIM"}

    def _ler_modo_evolucao(self, atual: Optional[str] = None) -> Optional[str]:
        """Mostra os modos mais comuns e permite digitar outro.

        Com ``atual`` informado, Enter mantém o valor atual.
        """
        print("\nModos de evolução:")
        for indice, modo in enumerate(MODOS_EVOLUCAO, start=1):
            print(f"  {indice} - {modo}")
        print(f"  {len(MODOS_EVOLUCAO) + 1} - Outro (digitar)")

        sufixo = f" [{atual}]" if atual else ""
        while True:
            texto = input(f"Escolha o modo de evolução{sufixo}: ").strip()
            if not texto and atual:
                return atual
            if texto.isdigit():
                opcao = int(texto)
                if 1 <= opcao <= len(MODOS_EVOLUCAO):
                    return MODOS_EVOLUCAO[opcao - 1]
                if opcao == len(MODOS_EVOLUCAO) + 1:
                    outro = input("Descreva o modo de evolução: ").strip()
                    if outro and len(outro) <= 50:
                        return outro
                    print("O modo deve ter entre 1 e 50 caracteres.")
                    continue
            print("Opção inválida.")

    def _ler_nivel(self, modo: str, atual: Optional[int] = None,
                   permitir_manter: bool = False) -> Optional[int]:
        """Nível é obrigatório quando o modo é 'Nível' e opcional nos demais."""
        obrigatorio = modo.strip().lower() == "nível"
        if permitir_manter:
            rotulo_atual = atual if atual is not None else "sem nível"
            dica = f" [{rotulo_atual}] (Enter mantém, 0 remove)"
        else:
            dica = " (obrigatório)" if obrigatorio else " (opcional, Enter para deixar vazio)"

        while True:
            texto = input(f"Nível de evolução{dica}: ").strip()
            if not texto:
                valor = atual if permitir_manter else None
            elif permitir_manter and texto == "0":
                valor = None
            else:
                try:
                    valor = int(texto)
                except ValueError:
                    print("Informe um número inteiro válido.")
                    continue
                if not NIVEL_MINIMO <= valor <= NIVEL_MAXIMO:
                    print(f"O nível deve estar entre {NIVEL_MINIMO} e {NIVEL_MAXIMO}.")
                    continue

            if obrigatorio and valor is None:
                print("Para o modo 'Nível' é obrigatório informar o nível.")
                continue
            return valor

    # ------------------------------------------------------------------
    # Consultas
    # ------------------------------------------------------------------
    def listar_evolucoes(self) -> bool:
        """Lista as evoluções com o nome dos Pokémons; retorna se havia registros."""
        return self._mostrar_tabela(
            self._consultar(self.QUERY_LISTAR + " ORDER BY e.id_evolucao"),
            "Nenhuma evolução cadastrada.",
        )

    def listar_pokemons(self) -> bool:
        return self._mostrar_tabela(
            self._consultar(self.QUERY_LISTAR_POKEMONS),
            "Nenhum Pokémon cadastrado. Cadastre Pokémons antes de inserir evoluções.",
        )

    def verifica_existencia(self, id_evolucao: int) -> bool:
        """Informa se o identificador de evolução já está cadastrado."""
        resultado = self._consultar(
            "SELECT 1 FROM tb_evolucao WHERE id_evolucao = %s",
            (id_evolucao,),
        )
        return not resultado.empty

    def _pokemon_existe(self, id_pokemon: int) -> bool:
        resultado = self._consultar(
            "SELECT 1 FROM tb_pokemon WHERE id_pokemon = %s",
            (id_pokemon,),
        )
        return not resultado.empty

    def _evolucao_duplicada(self, id_base: int, id_evoluido: int,
                            ignorar_id: Optional[int] = None) -> bool:
        """Impede cadastrar duas vezes a mesma ligação base -> evoluído."""
        resultado = self._consultar(
            """
            SELECT 1 FROM tb_evolucao
             WHERE id_pokemon_base = %s
               AND id_pokemon_evoluido = %s
               AND id_evolucao <> %s
            """,
            (id_base, id_evoluido, ignorar_id if ignorar_id is not None else -1),
        )
        return not resultado.empty

    def _proximo_id(self) -> int:
        resultado = self._consultar(
            "SELECT COALESCE(MAX(id_evolucao), 0) + 1 AS proximo FROM tb_evolucao"
        )
        return int(resultado.iloc[0]["proximo"]) if not resultado.empty else 1

    def _buscar_evolucao(self, id_evolucao: int):
        resultado = self._consultar(
            self.QUERY_LISTAR + " WHERE e.id_evolucao = %s",
            (id_evolucao,),
        )
        return None if resultado.empty else resultado.iloc[0]

    def _montar_evolucao(self, id_evolucao: int) -> Optional[Evolucao]:
        """Cria o objeto de domínio (com os objetos Pokémon associados)."""
        registro = self._buscar_evolucao(id_evolucao)
        if registro is None:
            return None
        nivel = registro["nivel_evolucao"]
        return Evolucao(
            id_evolucao=int(registro["id_evolucao"]),
            pokemon_base=Pokemon(
                id_pokemon=int(registro["id_pokemon_base"]),
                nome_pokemon=registro["pokemon_base"],
            ),
            pokemon_evoluido=Pokemon(
                id_pokemon=int(registro["id_pokemon_evoluido"]),
                nome_pokemon=registro["pokemon_evoluido"],
            ),
            nivel_evolucao=None if nivel is None or nivel != nivel else int(nivel),
            modo_evolucao=registro["modo_evolucao"],
        )

    def _ler_pokemon(self, mensagem: str, padrao: Optional[int] = None) -> Optional[int]:
        id_pokemon = self._ler_inteiro(mensagem, minimo=1, padrao=padrao)
        if not self._pokemon_existe(id_pokemon):
            print("O Pokémon informado não existe.")
            return None
        return id_pokemon

    # ------------------------------------------------------------------
    # Inserção
    # ------------------------------------------------------------------
    def _inserir_uma(self) -> Optional[Evolucao]:
        print("\n--- Inserir Evolução ---")
        if not self.listar_pokemons():
            return None

        sugestao = self._proximo_id()
        id_evolucao = self._ler_inteiro(
            f"ID da evolução [{sugestao}] (Enter usa o sugerido): ",
            minimo=1,
            padrao=sugestao,
        )
        if self.verifica_existencia(id_evolucao):
            print("Já existe uma evolução cadastrada com este ID.")
            return None

        id_base = self._ler_pokemon("ID do Pokémon base (antes de evoluir): ")
        if id_base is None:
            return None
        id_evoluido = self._ler_pokemon("ID do Pokémon evoluído (resultado): ")
        if id_evoluido is None:
            return None
        if id_base == id_evoluido:
            print("Um Pokémon não pode evoluir para ele mesmo.")
            return None
        if self._evolucao_duplicada(id_base, id_evoluido):
            print("Esta evolução (base -> evoluído) já está cadastrada.")
            return None

        modo = self._ler_modo_evolucao()
        nivel = self._ler_nivel(modo)

        try:
            PostgresQueries(can_write=True).write(
                """
                INSERT INTO tb_evolucao
                    (id_evolucao, id_pokemon_base, id_pokemon_evoluido,
                     nivel_evolucao, modo_evolucao)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (id_evolucao, id_base, id_evoluido, nivel, modo),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível inserir a evolução: {erro}")
            return None

        evolucao = self._montar_evolucao(id_evolucao)
        print("\nEvolução inserida com sucesso.")
        if evolucao:
            print(evolucao.to_string())
        return evolucao

    def inserir_evolucao(self) -> Optional[Evolucao]:
        """Insere evoluções até o usuário responder que não deseja mais."""
        ultima = None
        while True:
            ultima = self._inserir_uma() or ultima
            if not self._confirmar("\nDeseja inserir mais alguma evolução? (S/N): "):
                return ultima

    # ------------------------------------------------------------------
    # Atualização
    # ------------------------------------------------------------------
    def _atualizar_uma(self) -> Optional[Evolucao]:
        print("\n--- Atualizar Evolução ---")
        if not self.listar_evolucoes():
            return None
        id_evolucao = self._ler_inteiro("ID da evolução a atualizar: ", minimo=1)
        atual = self._buscar_evolucao(id_evolucao)
        if atual is None:
            print("Evolução não encontrada.")
            return None

        print("\nInforme os novos valores (Enter mantém o valor atual).")
        id_base = self._ler_pokemon(
            f"ID do Pokémon base [{atual['id_pokemon_base']} - {atual['pokemon_base']}]: ",
            padrao=int(atual["id_pokemon_base"]),
        )
        if id_base is None:
            return None
        id_evoluido = self._ler_pokemon(
            f"ID do Pokémon evoluído [{atual['id_pokemon_evoluido']} - {atual['pokemon_evoluido']}]: ",
            padrao=int(atual["id_pokemon_evoluido"]),
        )
        if id_evoluido is None:
            return None
        if id_base == id_evoluido:
            print("Um Pokémon não pode evoluir para ele mesmo.")
            return None
        if self._evolucao_duplicada(id_base, id_evoluido, ignorar_id=id_evolucao):
            print("Já existe outra evolução com este mesmo par base -> evoluído.")
            return None

        modo = self._ler_modo_evolucao(atual=atual["modo_evolucao"])
        nivel_atual = atual["nivel_evolucao"]
        nivel_atual = None if nivel_atual is None or nivel_atual != nivel_atual else int(nivel_atual)
        nivel = self._ler_nivel(modo, atual=nivel_atual, permitir_manter=True)

        try:
            PostgresQueries(can_write=True).write(
                """
                UPDATE tb_evolucao
                   SET id_pokemon_base = %s,
                       id_pokemon_evoluido = %s,
                       nivel_evolucao = %s,
                       modo_evolucao = %s
                 WHERE id_evolucao = %s
                """,
                (id_base, id_evoluido, nivel, modo, id_evolucao),
            )
        except (IntegrityError, DatabaseError) as erro:
            print(f"Não foi possível atualizar a evolução: {erro}")
            return None

        evolucao = self._montar_evolucao(id_evolucao)
        print("\nEvolução atualizada com sucesso.")
        if evolucao:
            print(evolucao.to_string())
        return evolucao

    def atualizar_evolucao(self) -> Optional[Evolucao]:
        """Atualiza evoluções até o usuário responder que não deseja mais."""
        ultima = None
        while True:
            ultima = self._atualizar_uma() or ultima
            if not self._confirmar("\nDeseja atualizar mais alguma evolução? (S/N): "):
                return ultima

    # ------------------------------------------------------------------
    # Exclusão
    # ------------------------------------------------------------------
    def _excluir_uma(self) -> bool:
        print("\n--- Excluir Evolução ---")
        if not self.listar_evolucoes():
            return False
        id_evolucao = self._ler_inteiro("ID da evolução a excluir: ", minimo=1)
        evolucao = self._montar_evolucao(id_evolucao)
        if evolucao is None:
            print("Evolução não encontrada.")
            return False

        print(evolucao.to_string())
        # Nenhuma tabela referencia TB_EVOLUCAO hoje, mas o fluxo padrão
        # confirma, verifica FKs e só então exclui.
        return excluir_registro_seguro(
            "tb_evolucao",
            id_evolucao,
            f"a evolução {evolucao.get_pokemon_base().get_nome_pokemon()} -> "
            f"{evolucao.get_pokemon_evoluido().get_nome_pokemon()}",
        )

    def excluir_evolucao(self) -> bool:
        """Exclui evoluções até o usuário responder que não deseja mais."""
        excluiu = False
        while True:
            excluiu = self._excluir_uma() or excluiu
            if not self._confirmar("\nDeseja excluir mais alguma evolução? (S/N): "):
                return excluiu
