from sqlalchemy import (
    Column, Integer, String, DateTime, func,
)

from src.domain.url import OriginUrl
from src.domain.url_repository import UrlRepository

from .sqlalchemy import Base


class SAUrlRepository(UrlRepository):
    def save(self, origin_url: OriginUrl) -> None:
        pass


class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    seq = Column(String, index=True, unique=True, nullable=False)
    origin = Column(String, nullable=False)
    shorten = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now)
    updated_at = Column(
            DateTime, nullable=False, default=func.now, onupdate=func.now)
