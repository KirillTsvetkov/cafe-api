from datetime import datetime

from pydantic.main import BaseModel

from .customer import CustomerBase, Customer
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
class CartBase(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True)
    cart_total = Column(Float, nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None, nullable=True)

class Cart(BaseModel):
    id: int
    customer_id: int
    cart_total: float
    customer: Customer = None
    class Config:
        orm_mode = True
class ReadAllCarts(BaseModel):
    carts: list[Cart]

class CartCreate(BaseModel):
    customer_id: int
