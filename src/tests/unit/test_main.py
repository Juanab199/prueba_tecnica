import pytest
from fastapi.testclient import TestClient

class TestMain:
    
    def test_read_main(self, client: TestClient):
        response = client.get("/v1/docs")
        assert response.status_code == 200
            
    def test_main(self, client:TestClient):
        response = client.post("/api/products", json={})
        assert response.status_code == 422
            
    def test_exception_handler_integrity(self, client:TestClient):
        json_data = {
            "sku":"2190",
            "name":"Agua 1500 ml",
            "price":10.60
        }
        response = client.post("/api/products", json=json_data)
        assert response.status_code == 400
        assert response.json() == {
            "detail": [
                {
                    "type": "IntegrityError",
                    "message": "El registro esta duplicado en la base de datos"
                }
            ]
        }   