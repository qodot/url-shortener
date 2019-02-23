from src.domain.url import UrlShortener


class TestUrlShortify:
    def test_shortify_short_length(self):
        url = UrlShortener()
        seq = str(99999999)

        shortified = url.shortify(seq)
        print(shortified)

        assert len(shortified) <= 11

    def test_shortify_unique(self):
        url = UrlShortener()

        shortifieds = []
        for seq in range(2222):
            seq = str(seq)

            shortified = url.shortify(seq)
            assert shortified not in shortifieds

            shortifieds.append(shortified)
