from typing import Optional
from pydantic import BaseModel, field_validator

class ProductSch(BaseModel):
    sku: str
    name: str
    price: float
    stock: Optional[int] = 100
    
    class Config:
        orm_mode = True
        json_schema_extra = {
            "ejemplo": {
                "sku": "1001A",
                "name": "nombre del producto",
                "stock": "stock inicial por defecto 100"
            }
        }

    @field_validator("sku", "name")
    def in_case_sku_empty(cls, value):
        if value == "":
            raise ValueError('El campo no puede estar vacío')
        return value
    
    @field_validator("stock")
    def in_case_stock_zero(cls, stock):
        if stock == 0:
            raise ValueError('No se puede agregar un stock de 0')
        return stock


class StockUpdate(BaseModel):
    stock: int
    
    @field_validator("stock")
    def in_case_stock_zero(cls, stock):
        if stock == 0:
            raise ValueError('No se puede agregar un stock de 0')
        return stock
    

class ProductOrdered(BaseModel):
    sku: str
    quantity: int
    
    @field_validator("sku")
    def in_case_sku_empty(cls, value):
        if value == "":
            raise ValueError('El campo no puede estar vacío')
        return value

class OrderSch(BaseModel):
    order_id: str
    products: list[ProductOrdered]
    
    @field_validator("order_id")
    def in_case_order_id_empty(cls, value):
        if value == "":
            raise ValueError('El campo no puede estar vacío')
        return value
    
    class Config:
        orm_mode = True
        json_schema_extra = {
            "ejemplo": {
                "peoduct_id": "1001A",
                "quantity": "1000",
            }
        }