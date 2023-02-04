from fastapi import APIRouter

router = APIRouter(
    prefix="/cart_item",
    tags=["CartItem"],
    responses={404: {"description": "Not found"}},
)