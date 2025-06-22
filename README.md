# Digital Wallet API

A RESTful API for a digital wallet system built with FastAPI, supporting user registration, login, fund transfers, transaction history, currency conversion, and product purchase using wallet balance.

## Features

* User Registration and Login (JWT Auth)
* Fund Account and Transfer to Other Users
* View Wallet Balance and Transaction History
* Currency Conversion (using external API)
* Buy Products Using Wallet Balance
* SQLite as Database
* Docker support
* Unit testing with `pytest`

---

## Project Structure

```
wallet_api/
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── database.py
├── auth.py
├── utils/
│   └── currency.py
├── routes/
│   ├── user.py
│   ├── wallet.py
│   └── product.py
├── tests/
│   └── test_wallet.py
├── .env
└── requirements.txt
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/wallet_api.git
cd wallet_api
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you encounter an error about `requirements.txt` missing, manually install:

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose python-dotenv httpx
```

### 4. Create `.env` file

```
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
EXCHANGE_RATE_API=https://api.exchangerate-api.com/v4/latest/USD
```

### 5. Run the server

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Testing

To run the unit tests:

```bash
pytest tests/
```

---

## Docker (Optional)

To build and run with Docker:

```bash
docker build -t wallet_api .
docker run -d -p 8000:8000 wallet_api
```

---

## API Endpoints

Visit Swagger UI at `/docs` or Redoc at `/redoc`.

---

## License

This project is licensed under the MIT License.



