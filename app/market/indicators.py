import requests
import pandas as pd

from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

from app.risk.atr import (
    calculate_atr
)
from ta.trend import ADXIndicator



def get_market_indicators(
    symbol,
    interval="1h"
):

    url = (
    "https://api.binance.com/api/v3/klines"
    f"?symbol={symbol}"
    f"&interval={interval}"
    f"&limit=200"
)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(
            f"Unable to connect to Binance:\n{e}"
        )

    # Continue with the rest of your code... 



    closes = [
        float(candle[4])
        for candle in data
    ]
    
    opens = [
    float(candle[1])
    for candle in data
]
    
    volumes = [
    float(candle[5])
    for candle in data
]

    highs = [
        float(candle[2])
        for candle in data
    ]

    lows = [
        float(candle[3])
        for candle in data
    ]

    df = pd.DataFrame(
        closes,
        columns=["close"]
    )

    df["high"] = highs
    df["low"] = lows

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

    atr = calculate_atr(
        df
    )
    df["adx"] = ADXIndicator(
    high=df["high"],
    low=df["low"],
    close=df["close"],
    window=14
).adx()
    latest = df.iloc[-1]

    return {
    "price": float(latest["close"]),
    "ema50": float(latest["ema50"]),
    "ema200": float(latest["ema200"]),
    "rsi": float(latest["rsi"]),
    "adx": float(latest["adx"]),
    "atr": atr,
    "closes": closes,
    "highs": highs,
    "lows": lows,
    "volumes": volumes,
    "opens": opens,
}