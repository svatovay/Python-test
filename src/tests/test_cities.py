from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
city = 'Москва'


def test_read_cities():
    response = client.get("/cities")
    assert response.status_code == 200


def test_read_city():
    response = client.get(f"/cities/{city}")
    assert response.status_code == 200
    assert list(response.json().keys()) == ['name', 'id', 'weather']


def test_add_city():
    response = client.post(f"/cities/?name={city}")
    assert response.status_code == 200
    assert response.json()['name'] == city
    assert list(response.json().keys()) == ['name', 'id', 'weather']
