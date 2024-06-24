from pydantic import BaseModel, field_validator

class Product:
    sku: str
    name: str
    stock: int
    
    @field_validator("stock", always=True)
    def check_stock(cls, stock:str):
        pass
    
class Order:
    product_i: str
    quantity: int