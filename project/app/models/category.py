from sqlmodel import SQLModel, Field, DateTime
from datetime import datetime

class CategoryBase(SQLModel):
    title: str = Field(nullable=False)
    created_at: datetime = Field(nullable=False,
        default=datetime.now())
    updated_at: datetime = Field(nullable=True,
        default=None)

class Category(CategoryBase, table=True):
    id: int = Field(default=None, primary_key=True)


class CategoryCreate(Category):
    pass