from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
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

