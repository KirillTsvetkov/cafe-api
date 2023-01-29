from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, DateTime
class CustomerBase(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at =Column(DateTime, default=None, nullable=True)
