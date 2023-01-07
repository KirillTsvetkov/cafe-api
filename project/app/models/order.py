import string
from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from project.app.models.food import Food

class OrderBase(SQLModel):
    code: string
    date: datetime
    total: float
    #status:

class Order(OrderBase, table=True):
    id: int = Field(default=None, primary_key=True)

class OrderCreate(OrderBase):
    pass