from contextlib import contextmanager

import pytest


@contextmanager
def pytest_not_raises(exception_class):
    try:
        yield
    except exception_class:
        raise pytest.fail('DID RAISE {}'.format(exception_class))
