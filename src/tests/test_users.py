from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_users():
    response = client.get("/users")
    assert response.status_code == 200


def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert list(response.json().keys()) == ['name', 'surname', 'age', 'id']


def test_add_user():
    response = client.post("/users/", json={'name': 'test', 'surname': 'testerov', 'age': 150})
    assert response.status_code == 200
    assert response.json()['name'] == 'test'
    assert list(response.json().keys()) == ['name', 'surname', 'age', 'id']
