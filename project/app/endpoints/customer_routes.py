from fastapi import APIRouter

router = APIRouter(
    prefix="/customer",
    tags=["Customer"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def add(customer: CustomerCreate, session: AsyncSession = Depends(get_session)):
    customer = CustomerBase(title=customer.title, phone=customer.customer)
    session.add(customer)
    await session.commit()
    await session.refresh(customer)
    return customer