from src.domain.url import UrlShortener, OriginUrl, ShortenHash
from src.domain.url_repository import UrlRepository
from src.infra.seq import PGSeqGenerator


class UrlShortenerService:
    _url_repository: UrlRepository

    def __init__(self, url_repository: UrlRepository) -> None:
        self._url_repository = url_repository

    def shortify(self, origin_url: OriginUrl) -> ShortenHash:
        url_shortener = UrlShortener(seq_generator=PGSeqGenerator())

        shorten_hash: ShortenHash
        seq: bytes
        shorten_hash, seq = url_shortener.shortify(origin=origin_url)

        self._save_url(origin_url, shorten_hash, seq)

        return shorten_hash

    def _save_url(
            self, origin: OriginUrl, shorten: ShortenHash, seq: bytes,
            ) -> None:
        self._url_repository.save(origin, shorten, seq)
