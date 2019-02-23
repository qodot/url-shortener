from __future__ import annotations
import base64
from dataclasses import dataclass

from src.domain.seq import SeqGenerator


class UrlShortener:
    _seq_generator: SeqGenerator

    def __init__(self, seq_generator: SeqGenerator) -> None:
        self._seq_generator = seq_generator

    def shortify(self, origin: OriginUrl) -> ShortenHash:
        seq: bytes = self._get_seq()
        encoded: bytes = base64.urlsafe_b64encode(seq)
        _hash: str = self._remove_url_unsafe_padding(encoded)

        return ShortenHash(_hash=_hash)

    def _get_seq(self) -> bytes:
        next_seq = self._seq_generator.get_next()
        return str(next_seq).encode()

    def _remove_url_unsafe_padding(self, url_unsafe: bytes) -> bytes:
        url_unsafe = url_unsafe.decode()
        return url_unsafe.replace('=', '')


@dataclass
class OriginUrl:
    _url: str


@dataclass
class ShortenHash:
    _hash: str

    @property
    def hash(self):
        return self._hash

    def __len__(self):
        return len(self._hash)
