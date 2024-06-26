from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    sku: str
    name: str
    stock: Optional[int] = 100
    
    class Config:
        orm_mode = True
        schema_extra = {
            "ejemplo": {
                "sku": "1001A",
                "name": "nombre del producto",
                "stock": "stock inicial por defecto 100"
            }
        }
    
class Order(BaseModel):
    product_id: str
    quantity: int
    
    class Config:
        orm_mode = True
        schema_extra = {
            "ejemplo": {
                "peoduct_id": "1001A",
                "quantity": "1000",
            }
        }