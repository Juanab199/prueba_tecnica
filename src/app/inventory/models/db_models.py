from sqlalchemy import Integer, String, Column, Text, Float

from app.db.config import Base

class Product(Base):
    __tablename__ = "Products"
    
    sku = Column(String(90), primary_key=True, index=True, unique=True)
    name = Column(String(50), unique=True)
    price = Column(Float)
    stock = Column(Integer)
    
    
class Order(Base):
    __tablename__ = "Orders"
    
    order_id = Column(String(50), primary_key=True, index=True, unique=True)
    ordered_products = Column(Text)