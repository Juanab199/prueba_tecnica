import logging
from fastapi import APIRouter

from app.inventory.schemas.entry_data_schemas import Product, Order

task_router = APIRouter(prefix="(/v1")

@task_router.post(
    path="/api/products"
)
async def create_product(product: Product):
    pass

@task_router.patch(
    path="/api/inventories/product/{product_id}"
)
async def update_stock(product_id: int):
    pass
    
@task_router.post(
    path="/api/products"
)
async def create_order(order: Order):
    pass