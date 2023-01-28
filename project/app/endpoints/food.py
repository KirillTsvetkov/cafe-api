from fastapi import APIRouter, Depends, Request
from app.models.food import FoodBase, Food, ReadAllFoodResponse, ReadAllFood
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncIterator, TYPE_CHECKING
from sqlalchemy.future import select
from typing import List
from sqlalchemy.orm import joinedload, sessionmaker
from datetime import datetime



router = APIRouter(
    prefix="/food",
    tags=["Food"],
    responses={404: {"description": "Not found"}},
)


async def read_all(FoodBase, session: AsyncSession) -> AsyncIterator[FoodBase]:
    stmt = select(FoodBase).options(joinedload(FoodBase.category, innerjoin=True))
    stream = await session.stream(stmt.order_by(FoodBase.id))
    async for row in stream:
        yield row.FoodBase

@router.get("/", response_model=ReadAllFoodResponse)
async def read_all(
    request: Request,
    use_case: ReadAllFood = Depends(ReadAllFood),
) -> ReadAllFoodResponse:
    return ReadAllFoodResponse(notes=[food async for food in use_case.execute()])




