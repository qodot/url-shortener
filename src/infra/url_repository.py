from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm.exc import NoResultFound

from src.domain.error import NotExistShortUrlError
from src.domain.url import OriginUrl
from src.domain.url import ShortenHash
from src.domain.url import Url
from src.domain.url_repository import UrlRepository
from src.infra.sqlalchemy import Base
from src.infra.sqlalchemy import Session


class SAUrlRepository(UrlRepository):
    def is_exist_origin(self, origin_url: str) -> bool:
        with Session.begin() as session:
            result = session.query(UrlDAO).filter(
                UrlDAO.origin == origin_url,
            ).first()

        if result:
            return True

        return False

    def save(self, url: Url) -> None:
        new_url: UrlDAO = UrlDAO.from_domain(url)

        with Session.begin() as session:
            session.add(new_url)

    def get_shorten_by_origin(self, origin: OriginUrl) -> ShortenHash:
        with Session.begin() as session:
            try:
                result: Url = session.query(Url).filter(
                        Url.origin == origin.url).one()
            except NoResultFound:
                raise NotExistShortUrlError

        return ShortenHash(result.shorten)

    def get_origin_by_shorten(self, shorten: ShortenHash) -> OriginUrl:
        with Session.begin() as session:
            try:
                result: Url = session.query(Url).filter(
                        Url.shorten == shorten.hash).one()
            except NoResultFound:
                raise NotExistShortUrlError

        return OriginUrl(result.origin)


class UrlDAO(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    seq = Column(String, unique=True, nullable=False, index=True)
    origin = Column(String, unique=True, nullable=False, index=True)
    shorten = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(
            DateTime, nullable=False, default=datetime.now,
            onupdate=datetime.now)

    @classmethod
    def from_domain(cls, url: Url) -> UrlDAO:
        return cls(
            seq=url.seq.seq,
            origin=url.origin.url,
            shorten=url.shorten.hash,
        )
