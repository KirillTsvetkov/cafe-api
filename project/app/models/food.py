from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, DateTime
from .category import Category


class FoodBase(SQLModel):
    title: str = Field(nullable=False)
    description: str
    category_id: int = Field(nullable=False, foreign_key="category.id")
    price: float = Field(nullable=False)
    created_at: datetime = Field(nullable=False,
        default=datetime.now())
    updated_at: datetime = Field(nullable=True,
        default=None)

class Food(FoodBase, table=True):
    id: int = Field(default=None, primary_key=True)
    category: Category = Relationship(back_populates="category")


class FoodCreate(FoodBase):
    pass