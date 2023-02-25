from datetime import datetime
from app.db import Base
from pydantic.main import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from .customer import Customer


class OrderBase(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)
    date = Column(DateTime)
    total = Column(Float, nullable=False)
    status = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    created_at = Column(DateTime, default=datetime.now())
    updated_at =Column(DateTime, default=None, nullable=True)

class Order(BaseModel):
    id: int
    code: str
    date: datetime
    total: float
    status: int
    customer: Customer
    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    customer_id: int
    code: str
    date: datetime
    total: float
    status: int
    customer_id: int