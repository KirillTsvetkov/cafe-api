from sqlmodel import SQLModel, Field, Relationship

from .customer import Customer


class CartBase(SQLModel):
    customer_id: int = Field(default=None, foreign_key="customer.id")

class Cart(CartBase, table=True):
    id: int = Field(default=None, primary_key=True)
    food: Customer = Relationship(back_populates="customer")

class CartCreate(CartBase):
    pass