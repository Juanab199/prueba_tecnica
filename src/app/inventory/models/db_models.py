from sqlalchemy import Integer, String, Column, Text, Float

from app.db.config import Base

class Product(Base):
    __tablename__ = "Products"
    
    sku = Column(String, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    
    
class Order(Base):
    __tablename__ = "Orders"
    
    order_id = Column(String, primary_key=True, index=True)
    ordered_products = Column(Text)
    total = Column(Float)