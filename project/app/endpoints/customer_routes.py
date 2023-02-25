from fastapi import APIRouter, Depends, Request
from app.models.customer import CustomerBase, Customer, CustomerCreate
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

router = APIRouter(
    prefix="/customer",
    tags=["Customer"],
    responses={404: {"description": "Not found"}},
)

@router.get("/",  response_model=List[Customer])
async def get_all(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(CustomerBase))
    customers = result.scalars().all()
    return [Customer(id=customer.id, phone=customer.phone) for customer in customers]

@router.post("/",  response_model=Customer)
async def add(customer: CustomerCreate, session: AsyncSession = Depends(get_session)):
    customer = CustomerBase(phone = customer.phone)
    session.add(customer)
    await session.commit()
    await session.refresh(customer)
    return customer