import pytest
from fastapi.testclient import TestClient

from app.database import reset_db
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def fresh_db():
    reset_db()


def test_register_merchant_returns_201():
    r = client.post("/merchants", json={"name": "Foot Locker", "email": "a@shop.com"})
    assert r.status_code == 201
    assert r.json() == {"id": 1, "name": "Foot Locker", "email": "a@shop.com"}


def test_register_invalid_email_returns_422():
    r = client.post("/merchants", json={"name": "X", "email": "nope"})
    assert r.status_code == 422


def test_register_blank_name_returns_422():
    r = client.post("/merchants", json={"name": "", "email": "b@shop.com"})
    assert r.status_code == 422