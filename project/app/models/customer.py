from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class CustomerBase(SQLModel):
    phone: str = Field(nullable=False)
    created_at: datetime = Field(nullable=False,
        default=datetime.now())
    updated_at: datetime = Field(nullable=True,
        default=None)

class Customer(CustomerBase, table=True):
    id: int = Field(default=None, primary_key=True)


class CustomerCreate(CustomerBase):
    pass