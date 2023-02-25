from fastapi import APIRouter
from app.endpoints import food_routes
from app.endpoints import category_routes
from app.endpoints import customer_routes

router = APIRouter()
router.include_router(category_routes.router)
router.include_router(food_routes.router)
router.include_router(customer_routes.router)