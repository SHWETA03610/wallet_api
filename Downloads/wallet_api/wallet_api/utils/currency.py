import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CURRENCY_API_KEY")
BASE_URL = "https://api.currencyapi.com/v3/latest"

def convert_currency(inr_amount: float, to_currency: str) -> float:
    params = {
        "apikey": API_KEY,
        "base_currency": "INR",
        "currencies": to_currency
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if "data" not in data or to_currency not in data["data"]:
        raise ValueError("Currency conversion failed")
    rate = data["data"][to_currency]["value"]
    return round(inr_amount * rate, 2)