from __future__ import annotations
import base62
from dataclasses import dataclass
from urllib.parse import urlparse

from src.domain.error import InvalidUrl
from src.domain.seq_generator import SeqGenerator, UrlSeq


def url_validator(url: str) -> None:
    try:
        result = urlparse(url)
    except Exception:
        raise InvalidUrl

    if not all([result.scheme, result.netloc]):
        raise InvalidUrl


class UrlShortener:
    _seq_generator: SeqGenerator

    def __init__(self, seq_generator: SeqGenerator) -> None:
        self._seq_generator = seq_generator

    def shortify(self, origin: OriginUrl) -> ShortenHash:
        seq: UrlSeq = self._get_seq()

        _hash: str = self._hashing(seq)
        shorten_hash = ShortenHash(_hash=_hash)

        return shorten_hash, seq

    def _get_seq(self) -> UrlSeq:
        next_seq: UrlSeq = self._seq_generator.get_next()

        return next_seq

    def _hashing(self, seq: UrlSeq) -> str:
        int_seq = int(seq.seq)
        hash_: str = base62.encode(int_seq)

        return hash_


@dataclass
class OriginUrl:
    _url: str

    def __init__(self, url: str) -> None:
        self._set_url(url)

    @property
    def url(self) -> str:
        return self._url

    def _set_url(self, url: str) -> None:
        try:
            url_validator(url)
        except InvalidUrl:
            raise
        else:
            self._url = url


@dataclass
class ShortenHash:
    _hash: str

    @property
    def hash(self) -> str:
        return self._hash

    def __len__(self) -> int:
        return len(self._hash)
