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

    def shortify(self, origin: str) -> str:
        if self.url_repository.is_exist_origin(origin):
            raise ValueError('duplicated origin url')

        seq: int = self.seq_generator.get_next()
        url = Url(origin, seq)
        self.url_repository.save(url)

        return url.shorten.hash

    def get_shorten_by_origin(self, origin: str) -> str:
        url: Url = self.url_repository.find_by_origin(origin)

        return url.shorten.hash

    def get_origin_by_shorten(self, shorten: str) -> str:
        url: Url = self.url_repository.find_by_shorten(shorten)

        return url.origin.url
