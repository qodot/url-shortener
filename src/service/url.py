from src.domain.seq_generator import SeqGenerator
from src.domain.url import Url
from src.domain.url_repository import UrlRepository
from src.infra.seq_generator import PGSeqGenerator


class UrlService:
    url_repository: UrlRepository
    seq_generator: PGSeqGenerator

    def __init__(
        self,
        url_repository: UrlRepository,
        seq_generator: SeqGenerator,
    ) -> None:
        self.url_repository = url_repository
        self.seq_generator = seq_generator

    def shortify(self, origin_url: str) -> str:
        if self._is_exist_origin(origin_url):
            raise ValueError('duplicated origin url')

        seq: int = self._get_next_seq()
        url = Url(origin_url, seq)

        self._save(url)

        return url.shorten.hash

    def _is_exist_origin(self, origin_url: str) -> bool:
        return self.url_repository.is_exist_origin(origin_url)

    def _get_next_seq(self) -> int:
        return self.seq_generator.get_next()

    def _save(self, url: Url) -> None:
        self.url_repository.save(url)

    # def get_shorten(self, origin_url: OriginUrl) -> ShortenHash:
    #     shorten_hash: ShortenHash = self._get_shorten_by_origin(origin_url)

    #     return shorten_hash

    # def _get_shorten_by_origin(self, origin_url: OriginUrl) -> ShortenHash:
    #     shorten: ShortenHash = self._url_repository.get_shorten_by_origin(
    #             origin_url)

    #     return shorten

    # def get_origin(self, shorten_hash: ShortenHash) -> OriginUrl:
    #     origin: OriginUrl = self._get_origin_by_shorten(shorten_hash)

    #     return origin

    # def _get_origin_by_shorten(self, shorten_hash: ShortenHash) -> OriginUrl:
    #     origin: OriginUrl = self._url_repository.get_origin_by_shorten(
    #             shorten_hash)

    #     return origin
