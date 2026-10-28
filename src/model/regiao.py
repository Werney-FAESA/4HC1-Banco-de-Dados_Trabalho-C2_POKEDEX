from __future__ import annotations

from typing import Optional


class Regiao:
    def __init__(
        self,
        id_regiao: Optional[int] = None,
        nome_regiao: Optional[str] = None,
        professor_responsavel: Optional[str] = None,
    ):
        self.set_id_regiao(id_regiao)
        self.set_nome_regiao(nome_regiao)
        self.set_professor_responsavel(professor_responsavel)

    def get_id_regiao(self) -> Optional[int]:
        return self.id_regiao

    def set_id_regiao(self, id_regiao: Optional[int]) -> None:
        self.id_regiao = id_regiao

    def get_nome_regiao(self) -> Optional[str]:
        return self.nome_regiao

    def set_nome_regiao(self, nome_regiao: Optional[str]) -> None:
        self.nome_regiao = nome_regiao

    def get_professor_responsavel(self) -> Optional[str]:
        return self.professor_responsavel

    def set_professor_responsavel(
        self, professor_responsavel: Optional[str]
    ) -> None:
        self.professor_responsavel = professor_responsavel

    def to_string(self) -> str:
        return (
            f"ID Região: {self.get_id_regiao()} | "
            f"Nome da Região: {self.get_nome_regiao()} | "
            f"Professor Responsável: {self.get_professor_responsavel()}"
        )
