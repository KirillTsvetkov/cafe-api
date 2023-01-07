from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from project.app.models.food import Food
from project.app.models.order import Order

class OrderItemBase(SQLModel):
    order_id: int = Field(default=None, foreign_key="order.id")
    food_id: int = Field(default=None, foreign_key="food.id")
    quantity: int
    subtotal: float



class OrderItem(OrderItemBase, table=True):
    id: int = Field(default=None, primary_key=True)
    food: Food = Relationship(back_populates="foods")
    order: Order = Relationship(back_populates="order")

class OrderItemCreate(OrderItem):
    pass