import redis

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)
r = redis.Redis(host="redis", port=6379)


def test_get_users():
    # Given
    response = client.get("/users")

    # Then
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_user():
    # Given
    response = client.get("/users/3")

    # Then
    assert response.status_code == 200
    assert response.json() == "offline"


def test_user_status_handler():
    # Given
    response = client.post("/users/1")

    # Then
    assert response.status_code == 200
    assert response.json() == "success"