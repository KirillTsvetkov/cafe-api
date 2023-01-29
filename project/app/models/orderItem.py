from .food import FoodBase
from .order import OrderBase
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
    updated_at =Column(DateTime, default=None, nullable=True)