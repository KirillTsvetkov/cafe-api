from fastapi import APIRouter
from app.models.cartItem import CartItemBase, CartItemCreate

router = APIRouter(
    prefix="/cart_item",
    tags=["CartItem"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def add(cartItem: CartItemCreate, session: AsyncSession = Depends(get_session)):
    cartItem = CartItemBase(
        cart_id=cartItem.cart_id, 
        food_id=cartItem.food_id,
        quantity=cartItem.quantity,
        subtotal=cartItem.subtotal
    )
    session.add(cartItem)
    await session.commit()
    await session.refresh(cartItem)
    return cartItem