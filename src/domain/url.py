from __future__ import annotations

import base62
from dataclasses import dataclass
from urllib.parse import urlparse

from src.domain.error import InvalidUrl


def url_validator(url: str) -> None:
    try:
        result = urlparse(url)
    except Exception:
        raise InvalidUrl

    if not all([result.scheme, result.netloc]):
        raise InvalidUrl


class Url:
    origin: OriginUrl
    seq: UrlSeq
    shorten: ShortenHash

    def __init__(self, origin: str, seq: int, shorten: str = None) -> None:
        self.origin = OriginUrl(origin)
        self.seq = UrlSeq(seq)

        if shorten is None:
            self.shorten = self._shortify()
        else:
            self.shorten = ShortenHash(hash=shorten)

    def _shortify(self) -> ShortenHash:
        int_seq = int(self.seq.seq)
        hash_: str = base62.encode(int_seq)

        return ShortenHash(hash=hash_)


@dataclass
class OriginUrl:
    url: str

    def __init__(self, url: str) -> None:
        try:
            url_validator(url)
        except InvalidUrl:
            raise
        else:
            self.url = url


@dataclass
class UrlSeq:
    seq: str


@dataclass
class ShortenHash:
    hash: str

    def __len__(self) -> int:
        return len(self.hash)
