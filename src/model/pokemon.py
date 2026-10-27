from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.regiao import Regiao


class Pokemon:
    def __init__(self,
                 id_pokemon: int | None = None,
                 nome_pokemon: str | None = None,
                 tipo_primario: str | None = None,
                 tipo_secundario: str | None = None,
                 nivel_base: int | None = None,
                 regiao: Regiao | None = None              
                  ):
        self.set_id_pokemon(id_pokemon)
        self.set_nome_pokemon(nome_pokemon)
        self.set_tipo_primario(tipo_primario)
        self.set_tipo_secundario(tipo_secundario)
        self.set_nivel_base(nivel_base)
        self.set_regiao(regiao)

    def set_id_pokemon(self, id_pokemon: int | None):
        self.id_pokemon = id_pokemon

    def set_nome_pokemon(self, nome_pokemon: str | None):
        self.nome_pokemon = nome_pokemon

    def set_tipo_primario(self, tipo_primario: str | None):
        self.tipo_primario = tipo_primario

    def set_tipo_secundario(self, tipo_secundario: str | None):
        self.tipo_secundario = tipo_secundario

    def set_nivel_base(self, nivel_base: int | None):
        self.nivel_base = nivel_base

    def set_regiao(self, regiao: Regiao | None):
        self.regiao = regiao

    def get_id_pokemon(self) -> int | None:
        return self.id_pokemon

    def get_nome_pokemon(self) -> str | None:
        return self.nome_pokemon

    def get_tipo_primario(self) -> str | None:
        return self.tipo_primario

    def get_tipo_secundario(self) -> str | None:
        return self.tipo_secundario

    def get_nivel_base(self) -> int | None:
        return self.nivel_base

    def get_regiao(self) -> Regiao | None:
        return self.regiao

    def to_string(self) -> str:
        regiao = self.get_regiao()
        nome_regiao = regiao.get_nome_regiao() if regiao else "N/A"
        return f"ID Pokémon: {self.get_id_pokemon()} | Nome: {self.get_nome_pokemon()} | Tipo Primário: {self.get_tipo_primario()} | Tipo Secundário: {self.get_tipo_secundario()} | Nível Base: {self.get_nivel_base()} | Região: {nome_regiao}"



