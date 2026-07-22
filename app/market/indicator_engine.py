import pandas as pd

from ta.trend import EMAIndicator
from ta.trend import ADXIndicator
from ta.momentum import RSIIndicator

from app.risk.atr import calculate_atr


class IndicatorEngine:

    @staticmethod
    def calculate(opens, highs, lows, closes, volumes):

        df = pd.DataFrame()

        df["open"] = opens
        df["high"] = highs
        df["low"] = lows
        df["close"] = closes
        df["volume"] = volumes

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

        df["adx"] = ADXIndicator(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            window=14
        ).adx()

        atr = calculate_atr(df)

        latest = df.iloc[-1]

        return {

            "price": float(latest["close"]),

            "ema50": float(latest["ema50"]),

            "ema200": float(latest["ema200"]),

            "rsi": float(latest["rsi"]),

            "adx": float(latest["adx"]),

            "atr": atr,

            "opens": opens,

            "highs": highs,

            "lows": lows,

            "closes": closes,

            "volumes": volumes,

        }