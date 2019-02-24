from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


class SeqGenerator(ABC):
    @abstractmethod
    def get_next(self) -> UrlSeq:
        pass


@dataclass
class UrlSeq:
    _seq: str

    @property
    def seq(self) -> str:
        return self._seq
