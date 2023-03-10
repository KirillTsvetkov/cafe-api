from pydantic.main import BaseModel
from .food import Food
from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey

class OrderItemBase(Base):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    food_id = Column(Integer, ForeignKey('food.id'))
    quantity = Column(Integer)
    subtotal = Column(Float)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None, nullable=True)

class OrderItem(BaseModel):
    id: int
    order_id: int
    food: Food
    quantity: int
    subtotal: float
    class Config:
        orm_mode = True

class OrderItemCreate(BaseModel):
    order_id: int
    food_id: int
    quantity: int
    subtotal: float