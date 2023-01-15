from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from .customer import Customer


class CartBase(SQLModel):
    customer_id: int = Field(foreign_key="customer.id")
    created_at: datetime
    updated_at: datetime

class Cart(CartBase, table=True):
    id: int = Field(primary_key=True)
    food: Customer = Relationship(back_populates="customer")
    created_at: datetime = Field(nullable=False,
        default=datetime.now())
    updated_at: datetime = Field(nullable=True,
        default=None)

class CartCreate(CartBase):
    pass