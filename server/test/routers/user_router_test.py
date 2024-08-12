import pytest
from flask import Flask
from flask.testing import FlaskClient
from src.routers.user_router import routes_user


@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(routes_user)
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def reset_users():
    global users
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"},
    }


def test_get_users(client: FlaskClient):
    response = client.get("/users")
    assert response.status_code == 200
    data = response.get_json()
    assert "1" in data
    assert data["1"]["name"] == "Alice"
    assert data["2"]["name"] == "Bob"


def test_get_user_by_id(client: FlaskClient):
    def reset_users():
        users.clear()
        reset_users()
        response = client.get("/users/1")
        assert response.status_code == 404
        new_user = {"name": "Alice", "email": "alice@example.com"}
        response = client.post("/users", json=new_user)
        assert response.status_code == 201
        response = client.get("/users/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["name"] == "Alice"


def test_create_user(client: FlaskClient):
    reset_users()
    new_user = {"name": "Charlie", "email": "charlie@example.com"}
    response = client.post("/users", json=new_user)
    assert response.status_code == 201
    data = response.get_json()
    user_id = data["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    user_data = response.get_json()
    assert user_data["name"] == "Charlie"
    assert user_data["email"] == "charlie@example.com"


def test_update_user(client: FlaskClient):
    reset_users()
    updated_user = {"name": "Alice Updated", "email": "alice_updated@example.com"}
    response = client.put("/users/1", json=updated_user)
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "User updated"
    response = client.put("/users/999", json=updated_user)
    assert response.status_code == 404
