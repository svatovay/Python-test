from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_picnics():
    response = client.get("/picnics", params={'datetime': '2022-09-08T00:15:00+04:00', 'past': True})
    assert response.status_code == 200
    assert list(response.json()[0].keys()) == ['id', 'city', 'time', 'users']


def test_add_picnic():
    response = client.post(f"/picnics/", params={'city_id': 1, 'time': '2022-09-08T00:15:00+04:00'})
    assert response.status_code == 200
    assert response.json()['city_id'] == 1
    assert list(response.json().keys()) == ['city_id', 'time', 'id']


def test_register_to_picnic():
    response = client.post("/picnics/register/", params={'user_id': 1, 'picnic_id': 1})
    assert response.status_code == 200
    assert list(response.json().keys()) == ['id', 'user', 'picnic_city', 'picnic_datetime']
