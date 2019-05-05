from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm.exc import NoResultFound

from src.domain.error import NotExistShortUrlError
from src.domain.url import Url
from src.domain.url_repository import UrlRepository
from src.infra.sqlalchemy import Base
from src.infra.sqlalchemy import Session


class SAUrlRepository(UrlRepository):
    def is_exist_origin(self, origin: str) -> bool:
        with Session.begin() as session:
            result: UrlDAO = session.query(UrlDAO).filter(
                UrlDAO.origin == origin,
            ).first()

        if result:
            return True

        return False

    def save(self, url: Url) -> None:
        new_url: UrlDAO = UrlDAO.from_domain(url)

        with Session.begin() as session:
            session.add(new_url)

    def find_by_origin(self, origin: str) -> Url:
        with Session.begin() as session:
            try:
                url: UrlDAO = session.query(UrlDAO).filter(
                    UrlDAO.origin == origin,
                ).one()
            except NoResultFound:
                raise NotExistShortUrlError

        return url.to_domain()

    def find_by_shorten(self, shorten: str) -> Url:
        with Session.begin() as session:
            try:
                url: UrlDAO = session.query(UrlDAO).filter(
                    UrlDAO.shorten == shorten,
                ).one()
            except NoResultFound:
                raise NotExistShortUrlError

        return url.to_domain()


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

    def to_domain(self) -> Url:
        return Url(self.origin, self.seq, self.shorten)
