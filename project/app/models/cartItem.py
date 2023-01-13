from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from .food import Food
from .cart import Cart

class CartItemBase(SQLModel):
    cart_id: int = Field(default=None, foreign_key="cart.id")
    food_id: int = Field(default=None, foreign_key="food.id")
    quantity: int
    subtotal: float



class CartItem(CartItemBase, table=True):
    id: int = Field(default=None, primary_key=True)
    food: Food = Relationship(back_populates="food")
    cart: Cart = Relationship(back_populates="cart")

class OrderItemCreate(CartItemBase):
    pass