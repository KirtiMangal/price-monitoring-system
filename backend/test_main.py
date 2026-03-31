from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_refresh():
    response = client.post("/refresh")
    assert response.status_code == 200


def test_products():
    response = client.get("/products")
    assert response.status_code == 200


def test_product_detail():
    client.post("/refresh")  # ensure data exists
    response = client.get("/products/1")
    assert response.status_code == 200


def test_analytics():
    response = client.get("/analytics")
    assert response.status_code == 200

def test_invalid_product():
    response = client.get("/products/999")
    assert response.status_code == 404


def test_filter_products():
    client.post("/refresh")
    response = client.get("/products?category=bags")
    assert response.status_code == 200