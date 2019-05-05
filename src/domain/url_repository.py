from abc import ABC, abstractmethod

from src.domain.url import Url


class UrlRepository(ABC):
    @abstractmethod
    def is_exist_origin(self, origin: str) -> bool:
        pass

    @abstractmethod
    def save(self, url: Url) -> None:
        pass

    @abstractmethod
    def find_by_origin(self, origin: str) -> Url:
        pass

    @abstractmethod
    def find_by_shorten(self, shorten: str) -> Url:
        pass
