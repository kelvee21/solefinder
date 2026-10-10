import pytest
from fastapi.testclient import TestClient

from app.database import reset_db
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def fresh_db():
    reset_db()


def test_add_shoe_returns_201():
    r = client.post("/shoes", json={"brand": "Nike", "model": "Air Zoom", "price": 120.0})
    assert r.status_code == 201
    assert r.json() == {"id": 1, "brand": "Nike", "model": "Air Zoom", "price": 120.0}


def test_add_shoe_blank_brand_returns_422():
    r = client.post("/shoes", json={"brand": "", "model": "Air Zoom", "price": 120.0})
    assert r.status_code == 422


def test_add_shoe_bad_price_returns_422():
    r = client.post("/shoes", json={"brand": "Nike", "model": "Air Zoom", "price": -5})
    assert r.status_code == 422


def test_list_shoes_returns_added_shoes():
    client.post("/shoes", json={"brand": "Nike", "model": "Air Zoom", "price": 120.0})
    client.post("/shoes", json={"brand": "Adidas", "model": "Superstar", "price": 90.0})
    r = client.get("/shoes")
    assert r.status_code == 200
    assert r.json() == [
        {"id": 1, "brand": "Nike", "model": "Air Zoom", "price": 120.0},
        {"id": 2, "brand": "Adidas", "model": "Superstar", "price": 90.0},
    ]


def test_list_shoes_empty_catalog_returns_empty_list():
    r = client.get("/shoes")
    assert r.status_code == 200
    assert r.json() == []
