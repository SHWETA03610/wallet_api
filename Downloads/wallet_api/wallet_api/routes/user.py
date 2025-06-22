from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
from models import User
from schemas import UserCreate
from crud import get_user_by_username, create_user

router = APIRouter()

@router.post("/register", status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    created_user = create_user(db, user.username, user.password)
    return {"message": "User registered"}
