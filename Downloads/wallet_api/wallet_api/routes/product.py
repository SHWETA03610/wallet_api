from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import get_current_user
from database import get_db
from models import User
from schemas import ProductCreate, BuyRequest
from crud import add_product, get_all_products, buy_product

router = APIRouter()

@router.post("/product", status_code=201)
def add_new_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    prod = add_product(db, product)
    return {"id": prod.id, "message": "Product added"}

@router.get("/product")
def list_products(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.post("/buy")
def buy_item(
    buy: BuyRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    tr
