import pytest

from src.service.url import UrlService
from src.infra.seq_generator import PGSeqGenerator
from src.infra.sqlalchemy import Session
from src.infra.url_repository import SAUrlRepository
from src.infra.url_repository import UrlDAO

from test import TestDB


class TestUrlService(TestDB):
    def test_shortify(self):
        origin_url = 'https://www.google.com'

        service = UrlService(SAUrlRepository(), PGSeqGenerator())
        shorten_hash: str = service.shortify(origin_url)

        assert len(shorten_hash) <= 10

    def test_shortify_save(self):
        origin_url = 'https://www.google.com'

        service = UrlService(SAUrlRepository(), PGSeqGenerator())
        service.shortify(origin_url)

        with Session.begin() as session:
            url = session.query(UrlDAO).filter(
                UrlDAO.origin == origin_url,
            ).first()

            assert url is not None

    def test_shortify_raise_duplicated(self):
        origin_url = 'https://www.google.com'
        service = UrlService(SAUrlRepository(), PGSeqGenerator())
        service.shortify(origin_url)

        with pytest.raises(ValueError):
            service.shortify(origin_url)

    def test_get_shorten_by_origin(self):
        origin_url = 'https://www.naver.com'
        service = UrlService(SAUrlRepository(), PGSeqGenerator())
        shorten_hash_before: str = service.shortify(origin_url)

        shorten_hash_after: str = service.get_shorten_by_origin(origin_url)

        assert shorten_hash_before == shorten_hash_after

    def test_get_origin_by_shorten(self):
        origin_url_in = 'https://www.naver.com'
        service = UrlService(SAUrlRepository(), PGSeqGenerator())
        shorten_hash: str = service.shortify(origin_url_in)

        origin_url_out: str = service.get_origin_by_shorten(shorten_hash)

        assert origin_url_in == origin_url_out
