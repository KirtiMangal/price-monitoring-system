from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    source = Column(String)
    current_price = Column(Float)

class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class PriceChangeEvent(Base):
    __tablename__ = "price_change_events"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    old_price = Column(Float)
    new_price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)