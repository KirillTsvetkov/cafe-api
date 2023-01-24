from datetime import datetime
from .customer import CustomerBase
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
class CartBase(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None, nullable=True)