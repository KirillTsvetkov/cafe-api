from fastapi import APIRouter, Depends
from app.models.category import Category, CategoryCreate
from app.db import get_session, init_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime

router = APIRouter(
    prefix="/category",
    tags=["Category"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Category])
async def get_all(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Category))
    categories = result.scalars().all()
    return [Category(id=category.id, title=category.title) for category in categories]

@router.post("/")
async def add(category: CategoryCreate, session: AsyncSession = Depends(get_session)):
    category = Category(title=category.title, created_at=datetime.now(),
                updated_at=None)
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category