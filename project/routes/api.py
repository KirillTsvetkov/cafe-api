from fastapi import APIRouter
from app.endpoints import food
from app.endpoints import category

router = APIRouter()
router.include_router(category.router)