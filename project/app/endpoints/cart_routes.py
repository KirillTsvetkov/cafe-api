from fastapi import APIRouter
from app.models.cart import CartBase, Cart, CartCreate

router = APIRouter(
    prefix="/cart",
    tags=["Cart"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def add(cart: CartCreate, session: AsyncSession = Depends(get_session)):
    cart = CartBase(customer_id=cart.customer_id)
    session.add(cart)
    await session.commit()
    await session.refresh(cart)
    return cart