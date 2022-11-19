import redis

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)
r = redis.Redis(host="redis", port=6379)


def test_get_users():
    # Given
    r.set(str("user1"), "online", 10)
    r.set(str("user2"), "online", 10)
    response = client.get("/users")

    # Then
    assert response.status_code == 200
    assert len(response.json()) == 2
