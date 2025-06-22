# 💸 Digital Wallet API - Project Summary

A backend system for a digital wallet built with **FastAPI** and **SQLite** that supports:

* ✅ User registration
* ✅ Wallet funding & transfers
* ✅ Currency conversion
* ✅ Product purchases
* ✅ Transaction history

---

## 🚀 Tech Stack

* **FastAPI** – Lightweight, async Python web framework
* **SQLite** – Embedded relational database
* **bcrypt** – Secure password hashing
* **currencyapi.com** – Live currency rates API
* **Uvicorn** – ASGI server for FastAPI

---

## 📦 Project Structure

```bash
wallet_api/
├── main.py                # FastAPI app entry
├── models.py              # SQLAlchemy models
├── schemas.py             # Pydantic schemas
├── database.py            # DB setup
├── auth.py                # Basic Auth handling
├── crud.py                # Business logic
├── init_db.py             # DB initialization
├── .env.example           # Env template
├── README.md
├── requirements.txt       # Dependencies
├── routes/
│   ├── user.py
│   ├── wallet.py
│   └── product.py
├── utils/
│   └── currency.py        # Currency conversion helper
└── tests/
    └── test_wallet.py
```

---

## 🔐 Authentication

All protected endpoints use **Basic Auth** with the `Authorization` header:

```http
Authorization: Basic base64(username:password)
```

Passwords are stored securely using **bcrypt**.

---

## 🛠️ Setup Instructions

```bash
# 1. Clone the repository
$ git clone <repo-url> && cd wallet_api

# 2. Create and activate a virtual environment
$ python -m venv venv
$ venv\Scripts\activate     # Windows

# 3. Install required packages
$ pip install -r requirements.txt

# 4. Setup .env file
$ copy .env.example .env
# Add your CURRENCY_API_KEY in .env

# 5. Initialize database
$ python init_db.py

# 6. Run the server
$ uvicorn main:app --reload
```

---

## 📡 API Endpoints Overview

| Method | Endpoint         | Description                       |
| ------ | ---------------- | --------------------------------- |
| POST   | `/register`      | Register new user (no auth)       |
| POST   | `/fund`          | Deposit money to wallet           |
| POST   | `/pay`           | Send money to another user        |
| GET    | `/bal?currency=` | View wallet balance in INR/USD... |
| GET    | `/stmt`          | Get transaction history           |
| POST   | `/product`       | Add a product                     |
| GET    | `/product`       | List all products                 |
| POST   | `/buy`           | Buy product using wallet funds    |

---

## 🌍 Currency Conversion

For balance in other currencies, conversion is powered by [currencyapi.com](https://currencyapi.com). Use your API key in `.env`:

```
CURRENCY_API_KEY=your_api_key_here
```

---

## ✅ Final Notes

* Built to be modular and readable
* Supports automated deployment (Render-ready)
* Secure, RESTful, and extendable backend

---

**Created by:** SHWETA PRAGYAN G ✨

Feel free to fork, star ⭐, and contribute!

