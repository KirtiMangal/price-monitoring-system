# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)

# headers = {
#     "x-api-key": "secret123"
# }


# def test_home():
#     response = client.get("/")
#     assert response.status_code == 200


# # def test_refresh():
# #     response = client.post("/refresh")
# #     assert response.status_code == 200

# client.post("/refresh")

# def test_products():
#     response = client.get("/products")
#     assert response.status_code == 200


# def test_product_detail():
#     client.post("/refresh")  # ensure data exists
#     response = client.get("/products/1")
#     assert response.status_code == 200


# def test_analytics():
#     response = client.get("/analytics")
#     assert response.status_code == 200

# def test_invalid_product():
#     response = client.get("/products/999")
#     assert response.status_code == 404


# def test_filter_products():
#     client.post("/refresh")
#     response = client.get("/products?category=bags")
#     assert response.status_code == 200



from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

headers = {
    "x-api-key": "secret123"
}


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_refresh():
    response = client.post("/refresh", headers=headers)
    assert response.status_code == 200


def test_products():
    response = client.get("/products", headers=headers)
    assert response.status_code == 200


def test_product_detail():
    client.post("/refresh", headers=headers)
    response = client.get("/products/1", headers=headers)
    assert response.status_code == 200


def test_analytics():
    response = client.get("/analytics", headers=headers)
    assert response.status_code == 200


def test_invalid_product():
    response = client.get("/products/999", headers=headers)
    assert response.status_code == 404


def test_filter_products():
    client.post("/refresh", headers=headers)
    response = client.get("/products?category=bags", headers=headers)
    assert response.status_code == 200