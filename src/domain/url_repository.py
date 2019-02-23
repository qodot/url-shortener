from abc import ABC, abstractmethod

from src.domain.url import OriginUrl, ShortenHash


class UrlRepository(ABC):
    @abstractmethod
    def save(
            self, origin_url: OriginUrl, shorten: ShortenHash, seq: bytes,
            ) -> None:
        pass
