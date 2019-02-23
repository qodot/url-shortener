from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

uri = f'postgresql://postgres:1234@localhost:5432/url-shortener'

engine = create_engine(uri, echo=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

Base = declarative_base()


@contextmanager
def tx():
    session = Session()

    try:
        yield session
    except Exception:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
