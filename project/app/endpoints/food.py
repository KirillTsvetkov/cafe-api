from fastapi import APIRouter, Depends
from app.models.food import FoodBase
from app.db import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime

router = APIRouter(
    prefix="/food",
    tags=["Food"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_all(session: AsyncSession = Depends(Session)):
    result = await session.execute(select(FoodBase))
    foods = result.scalars().all()
    return [FoodBase(id=food.id, title=food.title, description=food.description, price=food.price, category_id=food.category_id) for food in foods]

