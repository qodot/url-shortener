from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm.exc import NoResultFound

from src.domain.url import OriginUrl, ShortenHash
from src.domain.url_repository import UrlRepository
from src.domain.seq_generator import UrlSeq
from src.domain.error import NotExistShortUrlError
from src.infra.sqlalchemy import Base, tx


class SAUrlRepository(UrlRepository):
    def save(
            self, origin: OriginUrl, shorten: ShortenHash, seq: UrlSeq,
            ) -> None:
        new_url = Url(
                origin=origin.url, shorten=shorten.hash,
                seq=seq.seq)

        with tx() as session:
            session.add(new_url)

    def get_origin_by_shorten(self, shorten: ShortenHash) -> OriginUrl:
        with tx() as session:
            try:
                result: Url = session.query(Url).filter(
                        Url.shorten == shorten.hash).one()
            except NoResultFound:
                raise NotExistShortUrlError

        return OriginUrl(result.origin)


class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    seq = Column(String, unique=True, nullable=False, index=True)
    origin = Column(String, unique=True, nullable=False)
    shorten = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(
            DateTime, nullable=False, default=datetime.now,
            onupdate=datetime.now)
