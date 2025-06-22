# crud.py
from sqlalchemy.orm import Session
from models import User, Transaction, Product
from schemas import UserCreate, PayRequest, ProductCreate
from passlib.hash import bcrypt
from datetime import datetime

# ---------------- User Operations ----------------
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hash(user.password)
    db_user = User(username=user.username, password=hashed_password, balance=0.0)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ---------------- Wallet Operations ----------------
def fund_account(db: Session, user_id: int, amount: float):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.balance += amount
        transaction = Transaction(user_id=user_id, amount=amount, type="credit", timestamp=datetime.utcnow())
        db.add(transaction)
        db.commit()
        db.refresh(user)
    return user

def transfer_funds(db: Session, sender_id: int, receiver_username: str, amount: float):
    sender = db.query(User).filter(User.id == sender_id).first()
    receiver = db.query(User).filter(User.username == receiver_username).first()
    if sender and receiver and sender.balance >= amount:
        sender.balance -= amount
        receiver.balance += amount

        transaction_sender = Transaction(user_id=sender.id, amount=amount, type="debit", timestamp=datetime.utcnow())
        transaction_receiver = Transaction(user_id=receiver.id, amount=amount, type="credit", timestamp=datetime.utcnow())

        db.add(transaction_sender)
        db.add(transaction_receiver)
        db.commit()
        return {"msg": "Transfer successful"}
    return {"error": "Insufficient balance or invalid user"}

def get_balance(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    return {"balance": user.balance} if user else {"error": "User not found"}

def get_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()

# ---------------- Product Operations ----------------
def add_product(db: Session, product: ProductCreate):
    db_product = Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_all_products(db: Session):
    return db.query(Product).all()

def buy_product(db: Session, user_id: int, product_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    product = db.query(Product).filter(Product.id == product_id).first()

    if not user or not product:
        return {"error": "User or Product not found"}

    if user.balance < product.price:
        return {"error": "Insufficient balance"}

    user.balance -= product.price
    transaction = Transaction(user_id=user.id, amount=product.price, type="debit", timestamp=datetime.utcnow())
    db.add(transaction)
    db.commit()
    return {"msg": f"Product '{product.name}' purchased successfully"}

