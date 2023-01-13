from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models.food import Food, FoodCreate

app = FastAPI()


@app.get("/test")
async def pong():
    return {"test": "Hi!"}