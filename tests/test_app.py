""" Tests for fastapi endpoints module """

import pytest
from fastapi.testclient import TestClient

from app import app


def test_get_index() -> None:
    """
    Test calling to index.
    :return: None
    """
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Check documentation here -> /docs"}


@pytest.mark.parametrize(
    ("iso_date", "result"),
    (
        # Invalid date
        ("2010-01-01", {"error": ["UF values are available between 2013 and 2023"]}),
        ("2030-04-01", {"error": ["UF values are available between 2013 and 2023"]}),
        ("2020-03-40", {"error": ["day is out of range for month"]}),
        ("2020-02-30", {"error": ["day is out of range for month"]}),
        ("2020-30-01", {"error": ["month must be in 1..12"]}),
        ("2020-5-01", {"error": ["Invalid isoformat string: '2020-5-01'"]}),
        ("20200601", {"error": ["Invalid isoformat string: '20200601'"]}),
        # Valid input
        ("2020-09-01", {"value": "28.680,37"}),
        ("2020-10-01", {"value": "28.708,80"}),
        ("2020-11-01", {"value": "28.844,20"}),
        ("2020-12-01", {"value": "29.036,92"}),
    ),
)
def test_get_uf_endpoint(iso_date: str, result: dict) -> None:
    """
    Test /uf/{date} api endpoint.
    :param iso_date: Date in ISO format (str).
    :param result: Result from api (dict).
    :return: None
    """
    client = TestClient(app)
    response = client.get(f"/uf/{iso_date}")
    assert response.status_code == 200
    assert response.json() == result
