import pandas as pd

from ta.trend import EMAIndicator, ADXIndicator
from ta.momentum import RSIIndicator

from app.risk.atr import calculate_atr


class DatasetPreprocessor:
    """
    Computes all technical indicators ONCE
    for an entire historical dataset.
    """

    def process(self, df: pd.DataFrame):

        df = df.copy()

        # -----------------------
        # EMA
        # -----------------------

        df["ema50"] = EMAIndicator(
            close=df["close"],
            window=50
        ).ema_indicator()

        df["ema200"] = EMAIndicator(
            close=df["close"],
            window=200
        ).ema_indicator()

        # -----------------------
        # RSI
        # -----------------------

        df["rsi"] = RSIIndicator(
            close=df["close"]
        ).rsi()

        # -----------------------
        # ATR
        # -----------------------

        df["atr"] = calculate_atr(df)

        # -----------------------
        # ADX
        # -----------------------

        df["adx"] = ADXIndicator(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            window=14
        ).adx()

        return df