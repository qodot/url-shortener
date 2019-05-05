from abc import ABC, abstractmethod

from src.domain.url import OriginUrl
from src.domain.url import ShortenHash
from src.domain.url import Url


class UrlRepository(ABC):
    @abstractmethod
    def is_exist_origin(self, origin_url: str) -> bool:
        pass

    @abstractmethod
    def save(self, url: Url) -> None:
        pass

    @abstractmethod
    def get_shorten_by_origin(self, origin: OriginUrl) -> ShortenHash:
        pass

    @abstractmethod
    def get_origin_by_shorten(self, shorten: ShortenHash) -> OriginUrl:
        pass
