import pytest

from src.domain.error import InvalidUrl
from src.domain.url import url_validator, UrlShortener, OriginUrl, ShortenHash
from src.infra.seq_generator import PGSeqGenerator
from test import pytest_not_raises


class TestUrlValidator:
    def test_url_validator(self):
        url = 'https://www.google.com'

        with pytest_not_raises(InvalidUrl):
            url_validator(url)

    def test_url_validator_success_no_www(self):
        url = 'http://google.com'

        with pytest_not_raises(InvalidUrl):
            url_validator(url)

    def test_url_validator_fail_no_scheme(self):
        url = 'www.google.com'

        with pytest.raises(InvalidUrl):
            url_validator(url)


class TestUrlShortify:
    def test_shortify_short_length(self):
        url_shortener = UrlShortener(seq_generator=PGSeqGenerator())
        origin_url = OriginUrl('https://www.google.com')

        shorten_hash: ShortenHash = url_shortener.shortify(origin=origin_url)

        assert len(shorten_hash) <= 15

    # def test_shortify_unique(self):
    #     url_shortener = UrlShortener(seq_generator=PGSeqGenerator())

    #     hashs: List[ShortenHash] = []
    #     for seq in range(1000):
    #         origin_url = OriginUrl('www.google.com')

    #         shorten_hash: ShortenHash = url_shortener.shortify(seq)
    #         assert shorten_hash.hash not in hashs

    #         hashs.append(shorten_hash)
