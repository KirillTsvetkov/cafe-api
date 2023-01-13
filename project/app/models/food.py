from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from .category import Category


class FoodBase(SQLModel):
    title: str
    description: str
    category_id: int = Field(default=None, foreign_key="category.id")

class Food(FoodBase, table=True):
    id: int = Field(default=None, primary_key=True)
    category: Category = Relationship(back_populates="category")

class FoodCreate(FoodBase):
    pass