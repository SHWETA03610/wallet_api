from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import get_current_user
from database import get_db
from models import User
from schemas import FundRequest, PayRequest
from crud import fund_account, transfer_funds, get_balance, get_transactions
from utils.currency import convert_currency

router = APIRouter()

@router.post("/fund")
def fund_wallet(
    request: FundRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_balance = fund_account(db, current_user.id, request.amt)
    return {"balance": new_balance}

@router.post("/pay")
def pay_user(
    request: PayRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        new_balance = transfer_funds(db, current_user.id, request.to, request.amt)
        return {"balance": new_balance}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/bal")
def get_wallet_balance(
    currency: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    balance = get_balance(db, current_user.id)
    if currency:
        try:
            converted, symbol = convert_currency(balance, currency)
            return {"balance": converted, "currency": currency.upper()}
        except Exception as e:
            raise HTTPException(status_code=502, detail="Currency conversion failed")
    return {"balance": balance, "currency": "INR"}

@router.get("/stmt")
def statement(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_transactions(db, current_user.id)
