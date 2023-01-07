from typing import Optional

from sqlmodel import SQLModel, Field


class FoodBase(SQLModel):
    title: str
    description: str



class Food(FoodBase, table=True):
    id: int = Field(default=None, primary_key=True)


class FoodCreate(FoodBase):
    pass