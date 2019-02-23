from src.service.url import UrlShortenerService
from src.domain.url import OriginUrl, ShortenHash
from src.infra.url_repository import SAUrlRepository, Url
from src.infra.sqlalchemy import tx


class TestUrlShortenerShortify:
    def test_shortify(self):
        service = UrlShortenerService(SAUrlRepository())
        origin_url = OriginUrl('www.google.com')

        shorten_hash: ShortenHash = service.shortify(origin_url)

        assert len(shorten_hash) <= 15

        with tx() as session:
            url = session.query(Url).filter(
                    Url.origin == origin_url.url).first()
            assert url is not None
