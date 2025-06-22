# init_db.py
from database import Base, engine
from models import User, Transaction, Product
import os

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    db_file = "wallet.db"
    if os.path.exists(db_file):
        print(f"✅ Database file '{db_file}' created.")
    else:
        print("❌ Database file not found.")
    print("✅ Tables created successfully.")

