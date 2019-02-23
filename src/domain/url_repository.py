from abc import ABC, abstractmethod

from src.domain.url import OriginUrl


class UrlRepository(ABC):
    @abstractmethod
    def save(self, origin_url: OriginUrl) -> None:
        pass
