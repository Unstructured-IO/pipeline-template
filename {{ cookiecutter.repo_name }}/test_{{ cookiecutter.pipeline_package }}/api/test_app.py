import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def test_client():
    from prepline_{{ cookiecutter.pipeline_package }}.api.app import app

    return TestClient(app)


def test_healthcheck(test_client):
    response = test_client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"healthcheck": "HEALTHCHECK STATUS: EVERYTHING OK!"}
