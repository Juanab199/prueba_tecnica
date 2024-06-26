import logging
from typing import Any
from sqlalchemy.orm import Session

from app.common.execptions import NotFoundProduct, InsufficientProducts
from app.inventory.models.db_models import Product, Order
from app.inventory.schemas.entry_data_schemas import ProductSch, OrderSch, ProductOrdered


logger = logging.getLogger(__name__)

class DbController:
    def __init__(self, session: Session = None) -> Any:
        self.db_session = session

    def create_product(self, product: ProductSch) -> Product:
        product_to_save = Product(
            sku = product.sku,
            name = product.name,
            price = product.price,
            stock = product.stock 
        )
        
        self.db_session.add(product_to_save)
        self.db_session.commit()
        self.db_session.refresh(product_to_save)
        return product_to_save

    def get_product_by_id(self, product_sku: str) -> Product:
        found_product = self.db_session.query(Product).filter(Product.sku == product_sku).first()
        if found_product is None:
            raise NotFoundProduct
        return found_product    
    
    def update_product_stock(self, product_id: str, num_stock_to_add: int, add: str = True) -> Product:
        product_to_update: Product = self.get_product_by_id(product_sku=product_id)
        
        new_stock = product_to_update.stock + num_stock_to_add if add else product_to_update.stock - num_stock_to_add
        product_to_update.stock = new_stock
        
        self.db_session.commit()
        self.db_session.refresh(product_to_update)
        return product_to_update
    
    def update_products_to_sell(self, products_ordered: list[ProductOrdered]):
        product_skus = [product.sku for product in products_ordered]
        quantities = [product.quantity for product in products_ordered]
        products_found = self.db_session.query(Product).filter(Product.sku.in_(product_skus)).all()
        
        if len(products_ordered) > len(products_found):
            raise NotFoundProduct
        
        for product, quantity in zip(products_found, quantities):
            new_stock = product.stock - quantity
            
            if new_stock < 0:
                raise InsufficientProducts(f"Stock insuficiente para el producto: {product.name} (SKU: {product.sku})")
            
            if new_stock < 10:
                logging.warning(
                    f"El producto: {product.name} con sku: {product.sku} esta por agotarse"
                )  
            
            product.stock = new_stock
            
        self.db_session.commit()
    
    def create_order(self, order: OrderSch):
        self.update_products_to_sell(order.products)
        
        _order_to_save = Order(
            order_id = order.order_id,
            ordered_products = str(order.products)
        )
        self.db_session.add(_order_to_save)
        self.db_session.commit()
        self.db_session.refresh(_order_to_save)
        return _order_to_save
        