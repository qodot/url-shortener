import base62
from urllib.parse import urlparse

from src.domain.error import InvalidUrl


class Url:
    origin = None
    seq = None
    shorten = None

    def __init__(self, origin: str, seq: int, shorten: str = None) -> None:
        self.origin = OriginUrl(origin)
        self.seq = UrlSeq(seq)

        if shorten is None:
            self.shorten = self._shortify()
        else:
            self.shorten = ShortenHash(hash=shorten)

    def _shortify(self) -> "ShortenHash":
        int_seq = int(self.seq.seq)
        hash_ = base62.encode(int_seq)

        return ShortenHash(hash=hash_)


class OriginUrl:
    url = ""

    def __init__(self, url: str) -> None:
        try:
            url_validator(url)
        except InvalidUrl:
            raise
        else:
            self.url = url


class UrlSeq:
    seq = ""

    def __init__(self, seq: str):
        self.seq = seq


class ShortenHash:
    hash = ""

    def __init__(self, hash: str):
        self.hash = hash

    def __len__(self) -> int:
        return len(self.hash)


def url_validator(url: str) -> None:
    try:
        result = urlparse(url)
    except Exception:
        raise InvalidUrl

    if not all([result.scheme, result.netloc]):
        raise InvalidUrl
