from __future__ import annotations
import base62
from dataclasses import dataclass

from src.domain.seq_generator import SeqGenerator, UrlSeq


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

    @property
    def url(self) -> str:
        return self._url


@dataclass
class ShortenHash:
    _hash: str

    @property
    def hash(self) -> str:
        return self._hash

    def __len__(self) -> int:
        return len(self._hash)
