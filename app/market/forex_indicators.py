import pandas as pd

from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

from app.market.forex_client import get_forex_candles
from app.risk.atr import calculate_atr


def get_forex_indicators(symbol="EUR/USD"):

    data = get_forex_candles(symbol)

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

    highs = [
        float(x["high"])
        for x in data["values"]
    ]

    lows = [
        float(x["low"])
        for x in data["values"]
    ]

    # API returns newest candle first
    closes.reverse()
    highs.reverse()
    lows.reverse()

    df = pd.DataFrame({
        "close": closes,
        "high": highs,
        "low": lows
    })

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

    atr = calculate_atr(df)

    latest = df.iloc[-1]

    return {
        "price": float(latest["close"]),
        "ema50": float(latest["ema50"]),
        "ema200": float(latest["ema200"]),
        "rsi": float(latest["rsi"]),
        "atr": atr,
        "closes": closes
    }