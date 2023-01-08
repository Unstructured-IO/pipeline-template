import pytest

from fastapi.testclient import TestClient


@pytest.fixture()
def test_client():
    from prepline_{{ cookiecutter.pipeline_package }}.api.text_input import app

    return TestClient(app)


empty_files = []

files = [
    (
        "text_files",
        (
            "sample2.txt",
            open(
                "test_{{ cookiecutter.pipeline_package }}/test_docs/sample2.txt",
                "rb",
            ),
            "application/octet-stream",
        ),
    ),
    (
        "text_files",
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
    "files, output_format, output_schema, status_code, headers",
    [
        (empty_files, "application/json", "isd", 400, {}),
        (files, "application/json", "isd", 200, {}),
        (files, "text/csv", "isd", 200, {}),
        (files, "application/json", "label_studio", 200, {}),
        (files, "text/csv", "label_studio", 406, {"Accept": "text/html"}),
        ([files[0]], None, None, 200, {}),
        ([files[0]], None, None, 406, {"Accept": "text/html"}),
    ],
)
def test_pipeline_1(test_client, files, output_format, output_schema, status_code, headers):
    files = [
        *files,
        *([("output_format", (None, output_format))] if output_format else []),
        *([("output_schema", (None, output_schema))] if output_schema else []),
    ]
    response = test_client.post(
        "/{{ cookiecutter.pipeline_package }}/v0.0.1/text-input", files=files, headers=headers if headers else None
    )
    assert response.status_code == status_code


def test_healthcheck(test_client):
    response = test_client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"healthcheck": "HEALTHCHECK STATUS: EVERYTHING OK!"}
