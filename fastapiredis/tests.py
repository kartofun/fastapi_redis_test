from fastapi.testclient import TestClient
from .application import app

client = TestClient(app)


# Простенькие тесты, перегружать всеми возможными случаями не стал
def test_index():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"result": "hello!"}


def test_write_data():
    response = client.post("/write_data", params={"phone": 88005553555, "address": "Moscou"})

    assert response.status_code == 200
    assert response.json() == {"phone": 88005553555, "address": "Moscou"}


def test_check_data():
    response = client.get("/check_data",
                          params={"phone": 88005553555})

    assert response.status_code == 200
    assert response.json() == {"address": "Moscou"}


def test_update_data():
    response = client.post("/write_data", params={"phone": 88005553555, "address": "Paris"})

    assert response.status_code == 200
    assert response.json() == {"phone": 88005553555, "address": "Paris"}
