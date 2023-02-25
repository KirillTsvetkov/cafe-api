from fastapi import APIRouter, Depends
from app.models.category import CategoryBase, Category, CategoryCreate
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
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

@router.post("/",  response_model=Category)
async def add(category: CategoryCreate, session: AsyncSession = Depends(get_session)):
    category = CategoryBase(title = category.title)
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category