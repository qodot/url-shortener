import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


PG_URI = os.environ.get('URL_SHORTENER_PG_URI')
engine = create_engine(PG_URI, echo=True)
session_factory = sessionmaker(bind=engine, expire_on_commit=False)
scoped_session_factory = scoped_session(session_factory)

Base = declarative_base()


class Session:
    @staticmethod
    def get():
        session = scoped_session_factory()
        return session

    @staticmethod
    @contextmanager
    def begin():
        session = scoped_session_factory()

        try:
            yield session
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
        finally:
            session.remove()
