from typing import List

from src.domain.url import UrlShortener, OriginUrl, ShortenHash
from src.infra.seq import PGSeqGenerator


class TestUrlShortify:
    def test_shortify_short_length(self):
        url_shortener = UrlShortener(seq_generator=PGSeqGenerator())
        origin_url = OriginUrl('www.google.com')

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
