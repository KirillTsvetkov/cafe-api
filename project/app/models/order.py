from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class OrderBase(SQLModel):
    code: str
    date: datetime
    total: float
    status: int
    created_at: datetime = Field(nullable=False,
        default=datetime.now())
    updated_at: datetime = Field(nullable=True,
        default=None)

class Order(OrderBase, table=True):
    id: int = Field(default=None, primary_key=True)

class OrderCreate(OrderBase):
    pass