import pandas as pd

from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

from app.market.forex_client import (
    get_forex_candles
)


def get_forex_indicators(
    symbol="EUR/USD"
):

    data = get_forex_candles(
        symbol
    )

    print("FOREX API RESPONSE:")
    print(data)


    if "values" not in data:
        raise Exception(
            f"Forex API Error: {data}"
        )


    closes = [
        float(x["close"])
        for x in data["values"]
    ]

if "values" not in data:
    raise Exception(
        f"Forex API Error: {data}"
    )



    closes = [
        float(x["close"])
        for x in data["values"]
    ]


    closes.reverse()

    df = pd.DataFrame(
        closes,
        columns=["close"]
    )

    df["ema50"] = EMAIndicator(
        close=df["close"],
        window=50
    ).ema_indicator()

    df["ema200"] = EMAIndicator(
        close=df["close"],
        window=200
    ).ema_indicator()

    df["rsi"] = RSIIndicator(
        close=df["close"]
    ).rsi()

    latest = df.iloc[-1]

    return {
        "price": float(latest["close"]),
        "ema50": float(latest["ema50"]),
        "ema200": float(latest["ema200"]),
        "rsi": float(latest["rsi"]),
        "atr": 0,
        "closes": closes
    }