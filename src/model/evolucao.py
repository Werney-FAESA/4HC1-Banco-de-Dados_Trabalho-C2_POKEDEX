from model.pokemon import Pokemon


class Evolucao:
    def __init__(self,
                 id_evolucao: int | None = None,
                 pokemon_base: Pokemon | None = None,
                 pokemon_evoluido: Pokemon | None = None,
                 nivel_evolucao: int | None = None,
                 modo_evolucao: str | None = None):
        self.set_id_evolucao(id_evolucao)
        self.set_pokemon_base(pokemon_base)
        self.set_pokemon_evoluido(pokemon_evoluido)
        self.set_nivel_evolucao(nivel_evolucao)
        self.set_modo_evolucao(modo_evolucao)

    def set_id_evolucao(self, id_evolucao: int | None):
        self.id_evolucao = id_evolucao

    def set_pokemon_base(self, pokemon_base: Pokemon | None):
        self.pokemon_base = pokemon_base

    def set_pokemon_evoluido(self, pokemon_evoluido: Pokemon | None):
        self.pokemon_evoluido = pokemon_evoluido

    def set_nivel_evolucao(self, nivel_evolucao: int | None):
        self.nivel_evolucao = nivel_evolucao

    def set_modo_evolucao(self, modo_evolucao: str | None):
        self.modo_evolucao = modo_evolucao

    def get_id_evolucao(self) -> int | None:
        return self.id_evolucao

    def get_pokemon_base(self) -> Pokemon | None:
        return self.pokemon_base

    def get_pokemon_evoluido(self) -> Pokemon | None:
        return self.pokemon_evoluido

    def get_nivel_evolucao(self) -> int | None:
        return self.nivel_evolucao

    def get_modo_evolucao(self) -> str | None:
        return self.modo_evolucao

    def to_string(self) -> str:
        pokemon_base = self.get_pokemon_base()
        pokemon_evoluido = self.get_pokemon_evoluido()
        nome_pokemon_base = pokemon_base.get_nome_pokemon() if pokemon_base else "N/A"
        nome_pokemon_evoluido = pokemon_evoluido.get_nome_pokemon() if pokemon_evoluido else "N/A"
        return f"ID Evolução: {self.get_id_evolucao()} | ID Pokémon Base: {nome_pokemon_base} | ID Pokémon Evoluído: {nome_pokemon_evoluido} | Nível Evolução: {self.get_nivel_evolucao()} | Modo Evolução: {self.get_modo_evolucao()}"

                 

