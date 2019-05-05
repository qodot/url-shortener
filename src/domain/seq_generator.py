from abc import ABC, abstractmethod


class SeqGenerator(ABC):
    @abstractmethod
    def get_next(self) -> int:
        pass
