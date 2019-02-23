from src.domain.url import Url


class TestUrlShortify():
    def test_shortify_short_length(self):
        url = Url()
        seq = str(99999999)

        shortified = url.shortify(seq)
        print(shortified)

        assert len(shortified) <= 11

    def test_shortify_unique(self):
        url = Url()

        shortifieds = []
        for seq in range(1000):
            seq = str(seq)

            shortified = url.shortify(seq)
            assert shortified not in shortifieds

            shortifieds.append(shortified)
