import requests
import pandas as pd

from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

from app.risk.atr import (
    calculate_atr
)


def get_market_indicators(
    symbol="BTCUSDT",
    interval="1h"
):

    url = (
        f"https://api.binance.com/api/v3/klines"
        f"?symbol={symbol}"
        f"&interval={interval}"
        f"&limit=200"
    )

    data = requests.get(url).json()

    closes = [
        float(candle[4])
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

    latest = df.iloc[-1]

    return {
        "price": float(latest["close"]),
        "ema50": float(latest["ema50"]),
        "ema200": float(latest["ema200"]),
        "rsi": float(latest["rsi"]),
        "atr": atr,
        "closes": closes,
        "volumes": volumes
    }