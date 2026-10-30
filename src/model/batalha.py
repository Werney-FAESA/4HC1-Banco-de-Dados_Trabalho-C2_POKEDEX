from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.treinador import Treinador


class Batalha:
    def __init__(self,
                 id_batalha: int | None = None,
                 treinador_1: Treinador | None = None,
                 treinador_2: Treinador | None = None,
                 data_batalha: date | None = None,
                 vencedor: Treinador | None = None,
                 local_batalha: str | None = None):
        self.set_id_batalha(id_batalha)
        self.set_treinador_1(treinador_1)
        self.set_treinador_2(treinador_2)
        self.set_data_batalha(data_batalha)
        self.set_vencedor(vencedor)
        self.set_local_batalha(local_batalha)

    def set_id_batalha(self, id_batalha: int | None):
        self.id_batalha = id_batalha

    def set_treinador_1(self, treinador_1: Treinador | None):
        self.treinador_1 = treinador_1

    def set_treinador_2(self, treinador_2: Treinador | None):
        self.treinador_2 = treinador_2

    def set_data_batalha(self, data_batalha: date | None):
        self.data_batalha = data_batalha

    def set_vencedor(self, vencedor: Treinador | None):
        self.vencedor = vencedor

    def set_local_batalha(self, local_batalha: str | None):
        self.local_batalha = local_batalha

    def get_id_batalha(self) -> int | None:
        return self.id_batalha

    def get_treinador_1(self) -> Treinador | None:
        return self.treinador_1

    def get_treinador_2(self) -> Treinador | None:
        return self.treinador_2

    def get_data_batalha(self) -> date | None:
        return self.data_batalha

    def get_vencedor(self) -> Treinador | None:
        return self.vencedor

    def get_local_batalha(self) -> str | None:
        return self.local_batalha

    def to_string(self) -> str:
        t1 = self.get_treinador_1()
        t2 = self.get_treinador_2()
        vencedor = self.get_vencedor()
        nome_t1 = t1.get_nome_treinador() if t1 else "N/A"
        nome_t2 = t2.get_nome_treinador() if t2 else "N/A"
        nome_vencedor = vencedor.get_nome_treinador() if vencedor else "N/A"
        data = self.get_data_batalha()
        data_formatada = data.strftime("%d/%m/%Y") if data else "N/A"
        return (f"ID Batalha: {self.get_id_batalha()} | Treinador 1: {nome_t1} | "
                f"Treinador 2: {nome_t2} | Data: {data_formatada} | "
                f"Vencedor: {nome_vencedor} | Local: {self.get_local_batalha()}")
