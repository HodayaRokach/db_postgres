import pytest
from flask import Flask
from flask.testing import FlaskClient


from src.routers.image_router import routes_image


@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(routes_image)
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def reset_images():
    global images
    images = {
        1: {
            "url": "https://example.com/image1.jpg",
            "description": "Beautiful landscape",
        },
        2: {"url": "https://example.com/image2.jpg", "description": "City skyline"},
    }


def test_get_images(client: FlaskClient):
    reset_images()
    response = client.get("/images")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data["1"]["url"] == "https://example.com/image1.jpg"
    assert data["2"]["description"] == "City skyline"


def test_get_image(client: FlaskClient):
    reset_images()
    response = client.get("/images/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["url"] == "https://example.com/image1.jpg"

    response = client.get("/images/999")
    assert response.status_code == 404
    data = response.get_json()
    assert data["message"] == "Image not found"


def test_create_image(client: FlaskClient):
    reset_images()
    new_image = {"url": "https://example.com/image3.jpg", "description": "New image"}
    response = client.post("/images", json=new_image)
    assert response.status_code == 201
    data = response.get_json()
    image_id = data["id"]
    assert image_id == 3
    response = client.get(f"/images/{image_id}")
    data = response.get_json()
    assert data["url"] == "https://example.com/image3.jpg"


def test_update_image(client: FlaskClient):
    reset_images()
    updated_image = {
        "url": "https://example.com/image1-updated.jpg",
        "description": "Updated description",
    }
    response = client.put("/images/1", json=updated_image)
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Image updated"

    response = client.get("/images/1")
    data = response.get_json()
    assert data["url"] == "https://example.com/image1-updated.jpg"

    response = client.put("/images/999", json=updated_image)
    assert response.status_code == 404
    data = response.get_json()
    assert data["message"] == "Image not found"
