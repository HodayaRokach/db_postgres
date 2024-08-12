import pytest
from src.app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/api")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Image-Reduction"
