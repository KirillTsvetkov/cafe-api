from typing import Optional
from datetime import datetime
from app.db import Base
from .food import FoodBase
from .cart import CartBase
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

class CartItemBase(Base):
    __tablename__ = "cart_item"
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('cart.id'))
    food_id = Column(Integer, ForeignKey('food.id'))
    quantity = Column(Integer)
    subtotal = Column(Float)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None, nullable=True)
