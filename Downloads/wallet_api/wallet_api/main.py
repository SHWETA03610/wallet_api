from fastapi import FastAPI
from routes.user import router as user_router
from routes.wallet import router as wallet_router
from routes.product import router as product_router

app = FastAPI(title="Digital Wallet API")

app.include_router(user_router)
app.include_router(wallet_router)
app.include_router(product_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Digital Wallet API"}

