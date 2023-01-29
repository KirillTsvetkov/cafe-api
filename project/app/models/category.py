from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db import Base
from pydantic import BaseModel
from sqlalchemy.orm import relationship

class CategoryBase(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    food = relationship("FoodBase", back_populates="category", lazy=True)
    updated_at = Column(DateTime, default=None, nullable=True)

class Category(BaseModel):
    id: int = None
    title: str = None
    class Config:
        orm_mode = True