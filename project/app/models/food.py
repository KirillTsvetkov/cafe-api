from sqlalchemy.orm import sessionmaker, relationship, joinedload
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, select
from .category import Category
from pydantic import BaseModel
from app.db import Base, get_session
from fastapi import Depends
from typing import AsyncIterator, TYPE_CHECKING

if TYPE_CHECKING:
    from .food import FoodBase
class FoodBase(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    price = Column(Float, nullable=False)
    category = relationship("CategoryBase",  back_populates="food", lazy=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at =Column(DateTime, default=None, nullable=True)

class Food(BaseModel):
    id: int = None
    title: str = None
    description: str
    category_id: int
    price: float
    category: Category = None
    class Config:
        orm_mode = True


class ReadAllFoodResponse(BaseModel):
    food: list[Food]
