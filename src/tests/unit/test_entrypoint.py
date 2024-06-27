from fastapi.testclient import TestClient
import random

random_num = random.randint(0,110000000000)
class TestEntrypoint:
    
    def test_create_product(self, client: TestClient):
        json_data = {
            "sku":str(random_num), 
            "name": f"test_product_{random_num}", 
            "price": 10.0, 
            "stock": 100
        }
        response = client.post("/api/products", json=json_data)
        assert response.status_code == 201
        assert response.json() == {"status": "Ok", "msg": "Se ha creado correctamente el producto"}

    def test_add_stock(self, client: TestClient):
        response = client.patch(f"/api/inventories/product/2190", json={"stock": 50})
        assert response.status_code == 200
        assert response.json() == {"status": "Ok", "msg": "Se actualizo el stock del producto correctamente"}

    def test_add_stock_product_not_found(self, client: TestClient):
        response = client.patch(f"/api/inventories/product/1", json={"stock": 50})
        assert response.status_code == 404
        assert response.json() == {'detail': 'Product no encontrado para actualizar'}
    
    def test_create_order(self, client: TestClient):
        json_data = {
            "order_id": f"12NP{random_num}",
            "products": [
                {
                    "sku": "2190",
                    "quantity": 10
                }
            ]
        }
        response = client.post("/api/orders", json=json_data)
        assert response.status_code == 201
        assert response.json() == {"status": "Ok", "msg": "Se registro la venta correctamente"}

    def test_not_found_product(self, client: TestClient):
        json_data = {
            "order_id": f"12NP{random_num}",
            "products": [
                {
                    "sku": "1",
                    "quantity": 10
                }
            ]
        }
        response = client.post("/api/orders", json=json_data)
        assert response.status_code == 404
        assert response.json() == {"detail": "Producto no encontrado no se puede vender"}

    def test_insufficient_products(self, client: TestClient):
        json_data = {
            "order_id": f"12NP{random_num}",
            "products": [
                {
                    "sku": "2190",
                    "quantity": 100000
                }
            ]
        }
        response = client.post("/api/orders", json=json_data)
        assert response.status_code == 409
        assert response.json() == {"detail": "Productos insuficientes"}