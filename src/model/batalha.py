from datetime import date
from model.treinador import Treinador

class Batalha:
    def __init__(self,
                 id_batalha: int | None = None,
                 treinador1: Treinador | None = None,
                 treinador2: Treinador | None = None,
                 data_batalha: date | None = None,
                 vencedor: Treinador | None = None,
                 local_batalha: str | None = None):
        self.set_id_batalha(id_batalha)
        self.set_treinador1(treinador1)
        self.set_treinador2(treinador2)
        self.set_data_batalha(data_batalha)
        self.set_vencedor(vencedor)
        self.set_local_batalha(local_batalha)

    def set_id_batalha(self, id_batalha: int | None):
        self.id_batalha = id_batalha

    def set_treinador1(self, treinador1: Treinador | None):
        self.treinador1 = treinador1

    def set_treinador2(self, treinador2: Treinador | None):
        self.treinador2 = treinador2

    def set_data_batalha(self, data_batalha: date | None):
        self.data_batalha = data_batalha

    def set_vencedor(self, vencedor: Treinador | None):
        self.vencedor = vencedor

    def set_local_batalha(self, local_batalha: str | None):
        self.local_batalha = local_batalha


    def get_id_batalha(self) -> int | None:
        return self.id_batalha

    def get_treinador1(self) -> Treinador | None:
        return self.treinador1

    def get_treinador2(self) -> Treinador | None:
        return self.treinador2

    def get_data_batalha(self) -> date | None:
        return self.data_batalha

    def get_vencedor(self) -> Treinador | None:
        return self.vencedor

    def get_local_batalha(self) -> str | None:
        return self.local_batalha

    def to_string(self) -> str:
        treinador1 = self.get_treinador1()
        treinador2 = self.get_treinador2()
        vencedor = self.get_vencedor()
        nome_treinador1 = treinador1.get_nome_treinador() if treinador1 else "N/A"
        nome_treinador2 = treinador2.get_nome_treinador() if treinador2 else "N/A"
        nome_vencedor = vencedor.get_nome_treinador() if vencedor else "N/A"

        return f"ID Batalha: {self.get_id_batalha()} | Treinador 1: {nome_treinador1} | Treinador 2: {nome_treinador2} | Data da Batalha: {self.get_data_batalha()} | Vencedor: {nome_vencedor} | Local da Batalha: {self.get_local_batalha()}"