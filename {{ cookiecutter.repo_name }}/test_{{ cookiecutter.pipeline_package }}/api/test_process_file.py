import pytest

from fastapi.testclient import TestClient


@pytest.fixture()
def test_client():
    from prepline_{{ cookiecutter.pipeline_package }}.api.process_file import app

    return TestClient(app)


empty_files = []

files = [
    (
        "files",
        (
            "sample1.txt",
            open(
                "test_{{ cookiecutter.pipeline_package }}/test_docs/sample1.txt",
                "rb",
            ),
            "application/octet-stream",
        ),
    ),
    (
        "files",
        (
            "sample2.txt",
            open(
                "test_{{ cookiecutter.pipeline_package }}/test_docs/sample2.txt",
                "rb",
            ),
            "application/octet-stream",
        ),
    ),
]


@pytest.mark.parametrize(
    "files, some_parameters, status_code, headers",
    [
        (empty_files, 5, 400, {}),
        (files, 6, 200, {}),
        ([files[0]], 7, 200, {}),
        (files, 8, 406, {"Accept": "text/html"}),
    ],
)
def test_pipeline_1(test_client, files, some_parameters, status_code, headers):
    response = test_client.post(
        "/{{ cookiecutter.pipeline_package }}/v0.0.1/process-file",
        files=files,
        data={"some_parameters": some_parameters},
        headers=headers if headers else None,
    )
    assert response.status_code == status_code


@pytest.mark.skip(reason="/healthcheck does not exist for pipeline notebook api yet")
def test_healthcheck(test_client):
    response = test_client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"healthcheck": "HEALTHCHECK STATUS: EVERYTHING OK!"}
