import requests


def get_price(symbol="BTCUSDT"):

    url = (
        f"https://api.binance.com/api/v3/ticker/price"
        f"?symbol={symbol}"
    )

    response = requests.get(url)

    data = response.json()

    return float(data["price"])