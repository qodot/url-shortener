import pytest

from src.domain.error import InvalidUrl
from src.domain.url import Url
from src.domain.url import url_validator
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


class TestUrl:
    def test_create_url(self):
        seq_generator = PGSeqGenerator()
        seq = seq_generator.get_next()
        origin = 'https://www.google.com'

        url = Url(origin, seq)

        assert len(url.shorten) <= 10
