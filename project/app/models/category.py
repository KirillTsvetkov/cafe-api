from sqlmodel import SQLModel, Field

class CategoryBase(SQLModel):
    title: str

class Category(CategoryBase, table=True):
    id: int = Field(default=None, primary_key=True)

class CategoryCreate(Category):
    pass