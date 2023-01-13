from sqlmodel import SQLModel, Field, Relationship

class CustomerBase(SQLModel):
    phone: str

class Customer(CustomerBase, table=True):
    id: int = Field(default=None, primary_key=True)


class CustomerCreate(CustomerBase):
    pass