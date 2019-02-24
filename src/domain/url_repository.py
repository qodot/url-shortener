from abc import ABC, abstractmethod

from src.domain.url import OriginUrl, ShortenHash
from src.domain.seq import UrlSeq


class UrlRepository(ABC):
    @abstractmethod
    def save(
            self, origin_url: OriginUrl, shorten: ShortenHash, seq: UrlSeq,
            ) -> None:
        pass
