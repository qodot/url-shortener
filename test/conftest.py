import os

from alembic.config import Config as AlembicConfig
from alembic.command import upgrade as alembic_upgrade
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


@pytest.fixture(scope='session')
def sa_engine():
    PG_URI = os.environ.get('URL_SHORTENER_PG_URI')
    engine = create_engine(PG_URI, echo=True)

    yield engine

    engine.dispose()


@pytest.fixture(scope='session')
def sa_session_factory(sa_engine):
    session_factory = sessionmaker(bind=sa_engine, expire_on_commit=False)
    Session = scoped_session(session_factory)

    yield Session


@pytest.fixture(scope='function')
def sa_session(sa_session_factory):
    session_obj = sa_session_factory()

    yield session_obj

    sa_session_factory.remove()


@pytest.fixture(scope='session', autouse=True)
def alembic_upgrade_head(sa_engine):
    alembic_config = AlembicConfig('alembic.ini')
    alembic_upgrade(alembic_config, 'head')
