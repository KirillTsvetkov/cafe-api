from fastapi import APIRouter, Depends
from app.models.category import CategoryBase, Category
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from typing import List

router = APIRouter(
    prefix="/category",
    tags=["Category"],
    responses={404: {"description": "Not found"}},
)

@router.get("/",  response_model=List[Category])
async def get_all(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(CategoryBase))
    categories = result.scalars().all()
    return [Category(id=category.id, title=category.title) for category in categories]