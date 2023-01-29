from fastapi import APIRouter, Depends, Request
from app.models.food import FoodBase, Food, FoodCreate
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload, sessionmaker
from datetime import datetime



router = APIRouter(
    prefix="/food",
    tags=["Food"],
    responses={404: {"description": "Not found"}},
)

async def get_all_food(session: AsyncSession) -> list[Food]:
    result = await session.execute(select(FoodBase).options(joinedload(FoodBase.category, innerjoin=True)))
    return result.scalars().all()


@router.get("/", response_model=list[Food])
async def get_all(session: AsyncSession = Depends(get_session)):
    food = await get_all_food(session)
    return [
        Food(title=f.title, description=f.description, category_id=f.category_id, price=f.price, category=f.category)
        for f in food
    ]

@router.post("/")
async def add(food: FoodCreate, session: AsyncSession = Depends(get_session)):
    food = FoodBase(title=food.title, description=food.description,
                price=food.price, category_id=food.category_id,
                created_at=datetime.now(), updated_at=None)
    session.add(food)
    await session.commit()
    await session.refresh(food)
    return food



