from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from routes.api import router as api_router

app = FastAPI()

app.include_router(api_router)
@app.get("/test")
async def pong():
    return {"test": "Hi!"}