import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup():
    old_environ = dict(os.environ)
    os.environ.update(
        {
            'PIPELINE_API_RATE_LIMIT': '999/second'
        }
    )
    yield
    os.environ.clear()
    os.environ.update(old_environ)
