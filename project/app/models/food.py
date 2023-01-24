from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from .category import CategoryBase
from app.db import Base


class FoodBase(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at =Column(DateTime, default=None, nullable=True)
