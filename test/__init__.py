from contextlib import contextmanager

import pytest


@contextmanager
def pytest_not_raises(exception_class):
    try:
        yield
    except exception_class:
        raise pytest.fail('DID RAISE {}'.format(exception_class))


def dont_commit(session):
    @contextmanager
    def fake_begin():
        yield session

    return fake_begin


class TestDB:
    @pytest.fixture(scope='function', autouse=True)
    def session_lifecycle(self, mocker, sa_session_factory, sa_session):
        mocker.patch(
            'src.infra.sqlalchemy.Session.begin',
            new=dont_commit(sa_session),
        )
