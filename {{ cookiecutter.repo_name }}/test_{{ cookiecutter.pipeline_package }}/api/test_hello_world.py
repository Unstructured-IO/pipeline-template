import pytest

from fastapi.testclient import TestClient


@pytest.fixture()
def test_client():
    from prepline_{{ cookiecutter.pipeline_package }}.api.hello_world import app
    return TestClient(app)


empty_files = []

files=[
  ('files',('pepg-S-1-1835597-000119312522106884.xbrl',open('test_{{ cookiecutter.pipeline_package }}/test_docs/pepg-S-1-1835597-000119312522106884.xbrl','rb'),'application/octet-stream')),
  ('files',('rgld-10-K-85535-000155837021011343.xbrl',open('test_{{ cookiecutter.pipeline_package }}/test_docs/rgld-10-K-85535-000155837021011343.xbrl','rb'),'application/octet-stream'))
]


@pytest.mark.parametrize(
    "files, some_parameters, status_code, headers", 
    [
        (empty_files, 5, 400, {}), 
        (files, 6, 200, {}), 
        ([files[0]], 7, 200, {}), 
        (files, 8, 406, {'Accept': 'text/html'})
    ]
)
def test_pipeline_1(test_client, files, some_parameters, status_code, headers):
    files = [
        *files,
        ('some_parameters', (None, some_parameters))
    ]
    response = test_client.post(
        "/{{ cookiecutter.pipeline_package }}/v0.0.1/hello-world",
        files=files,
        headers=headers if headers else None
    )
    assert response.status_code == status_code


def test_healthcheck(test_client):
    response = test_client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"healthcheck": "HEALTHCHECK STATUS: EVERYTHING OK!"}
