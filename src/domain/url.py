import base64

from dataclasses import dataclass


class UrlShortener:
    def shortify(self, seq: str) -> str:
        encoded: bytes = base64.urlsafe_b64encode(seq.encode())
        encoded: str = self._remove_url_unsafe_padding(encoded)

        return encoded

    def _remove_url_unsafe_padding(self, url_unsafe: bytes) -> bytes:
        url_unsafe = url_unsafe.decode()
        return url_unsafe.replace('=', '')


@dataclass
class OriginUrl:
    url: str
