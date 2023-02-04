from fastapi import APIRouter

router = APIRouter(
    prefix="/order_item",
    tags=["OrderItem"],
    responses={404: {"description": "Not found"}},
)