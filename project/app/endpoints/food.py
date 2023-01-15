from fastapi import APIRouter, Depends
from app.models.food import Food, FoodCreate
from app.db import get_session, init_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime

router = APIRouter(
    prefix="/food",
    tags=["Food"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Food])
async def get_all(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Food))
    foods = result.scalars().all()
    return [Food(id=food.id, title=food.title, description=food.description, price=food.price, category_id=food.category_id) for food in foods]

@router.post("/")
async def add(food: FoodCreate, session: AsyncSession = Depends(get_session)):
    food = Food(title=food.title, description=food.description,
                price=food.price, category_id=food.category_id,
                created_at=datetime.now(), updated_at=None)
    session.add(food)
    await session.commit()
    await session.refresh(food)
    return food