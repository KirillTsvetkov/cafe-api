from fastapi import APIRouter
from app.endpoints import food
from app.endpoints import category

router = APIRouter()
router.include_router(category.router)
router.include_router(food.router)