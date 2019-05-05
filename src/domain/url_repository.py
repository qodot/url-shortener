from abc import ABC, abstractmethod

from src.domain.url import OriginUrl
from src.domain.url import ShortenHash
from src.domain.url import UrlSeq


class UrlRepository(ABC):
    @abstractmethod
    def save(
            self, origin_url: OriginUrl, shorten: ShortenHash, seq: UrlSeq,
            ) -> None:
        pass

    @abstractmethod
    def get_shorten_by_origin(self, origin: OriginUrl) -> ShortenHash:
        pass

    @abstractmethod
    def get_origin_by_shorten(self, shorten: ShortenHash) -> OriginUrl:
        pass

    @abstractmethod
    def is_exist_origin(self, origin_url: OriginUrl) -> bool:
        pass
