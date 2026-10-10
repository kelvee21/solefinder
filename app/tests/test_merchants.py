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