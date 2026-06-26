import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv(
    "TWELVEDATA_API_KEY"
)


def get_forex_candles(
    symbol="EUR/USD"
):

    url = (
        "https://api.twelvedata.com/time_series"
        f"?symbol={symbol}"
        "&interval=1h"
        "&outputsize=200"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    return response.json()