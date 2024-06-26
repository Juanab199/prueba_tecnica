from typing import Any
from sqlalchemy.orm import Session

from app.inventory.models.db_models import Product
from app.inventory.schemas.entry_data_schemas import ProductSch

class DbController:
    def __init__(self, session: Session) -> Any:
        self.db_session = session

    def create_product(self, product: ProductSch) -> Product:
        _product_to_save = Product(
            sku = product.sku,
            name = product.name,
            price = product.price,
            stock = product.stock 
        )
        
        self.db_session.add(_product_to_save)
        self.db_session.commit()
        self.db_session.refresh(_product_to_save)
        return _product_to_save

    def get_product_by_id(self, product_sku: str) -> Product:
        return self.db_session.query(Product).filter(Product.sku == product_sku)
    
    def update_product_stock(self, product_id: str, new_stock: int) -> Product:
        _product_to_update: Product = self.get_product_by_id(product_sku=product_id)
        _product_to_update.stock = new_stock
        self.db_session.commit()
        self.db_session.refresh()
        return _product_to_update
    
    #def create_order(self, order_id: str, ordered_products: list[ProductSch]):
        
        