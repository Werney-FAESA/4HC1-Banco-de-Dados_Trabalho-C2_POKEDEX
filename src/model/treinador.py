from model.regiao import Regiao

class Treinador:
    def __init__(self,
                 id_treinador: int | None = None,
                 nome_treinador: str | None = None,
                 regiao: Regiao | None = None,
                 idade: int | None = None):
        self.set_id_treinador(id_treinador)
        self.set_nome_treinador(nome_treinador)
        self.set_regiao(regiao)
        self.set_idade(idade)

    def set_id_treinador(self, id_treinador: int | None):
        self.id_treinador = id_treinador

    def set_nome_treinador(self, nome_treinador: str | None):
        self.nome_treinador = nome_treinador

    def set_regiao(self, regiao: Regiao | None):
        self.regiao = regiao

    def set_idade(self, idade: int | None):
        self.idade = idade

    def get_idade(self) -> int | None:
        return self.idade

    def get_id_treinador(self) -> int | None:
        return self.id_treinador

    def get_nome_treinador(self) -> str | None:
        return self.nome_treinador

    def get_regiao(self) -> Regiao | None:
        return self.regiao

    def to_string(self) -> str:
        regiao = self.get_regiao()
        nome_regiao = regiao.get_nome_regiao() if regiao else "N/A"
        idade = self.get_idade() if self.get_idade() is not None else "N/A"

        return f"ID Treinador: {self.get_id_treinador()} | Nome: {self.get_nome_treinador()} | Região: {nome_regiao} | Idade: {idade}"
