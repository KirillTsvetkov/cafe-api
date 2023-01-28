from __future__ import annotations
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, select
from sqlalchemy.orm import relationship, joinedload, sessionmaker
from .category import Category
from pydantic import BaseModel
from app.db import Base, get_session
from fastapi import Depends
from typing import AsyncIterator, TYPE_CHECKING
from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
    from .food import FoodBase

class FoodBase(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    price = Column(Float, nullable=False)
    category = relationship("CategoryBase",  back_populates="food", lazy=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at =Column(DateTime, default=None, nullable=True)

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[FoodBase]:
        stmt = select(cls).options(joinedload(cls.category, innerjoin=True))
        stream = await session.stream(stmt.order_by(cls.id))
        async for row in stream:
            yield row.FoodBase

class Food(BaseModel):
    id: int = None
    title: str = None
    description: str
    category_id: int
    price: float
    category: Category = None
    class Config:
        orm_mode = True


class ReadAllFoodResponse(BaseModel):
    food: list[Food]

class ReadAllFood:
    def __init__(self, session: sessionmaker = Depends(get_session)) -> None:
        self.async_session = session

    async def execute(self) -> AsyncIterator[Food]:
        async with self.async_session() as session:
            async for note in FoodBase.read_all(session):
                yield Food.from_orm(note)