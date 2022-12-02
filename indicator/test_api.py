import redis

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)
r = redis.Redis(host="redis", port=6379)


def test_get_users():
    # Given
    r.set(str("1"), "online", 10)
    r.set(str("2"), "online", 10)
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


# def test_user_status_handler(user_id):
#     r.set(str(user_id), "online", 10)
#     return "success"
#     # Given
#     r.set(str("user1"), "online", 10)
#     r.set(str("user2"), "online", 10)
#     response = client.get("/users")

#     # Then
#     assert response.status_code == 200
#     assert len(response.json()) == 2