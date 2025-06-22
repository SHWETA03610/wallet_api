from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ---------------------------
# User Registration Schema
# ---------------------------
class UserCreate(BaseModel):
    username: str
    password: str

# ---------------------------
# Fund Wallet Schema
# ---------------------------
class FundRequest(BaseModel):
    amt: float

# ---------------------------
# Pay Another User Schema
# ---------------------------
class PayRequest(BaseModel):
    to: str
    amt: float

# ---------------------------
# Transaction Schema (used in /stmt)
# ---------------------------
class TransactionOut(BaseModel):
    kind: str  # "credit" or "debit"
    amt: float
    updated_bal: float
    timestamp: datetime

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2

# ---------------------------
# Add Product Schema
# ---------------------------
class ProductCreate(BaseModel):
    name: str
    price: float
    description: str

# ---------------------------
# Output Schema for Products
# ---------------------------
class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    description: str

    class Config:
        from_attributes = True

# ---------------------------
# Buy Product Schema
# ---------------------------
class BuyRequest(BaseModel):
    product_id: int
