import numpy as np


class MarketRegimeEngine:

    """
    Detects the current market environment.
    """

    def analyze(
        self,
        ema50,
        ema200,
        adx,
        atr,
        closes,
    ):

        trend = "RANGE"

        volatility = "NORMAL"

        # -----------------------------
        # Trend
        # -----------------------------

        if ema50 > ema200:

            trend = "UPTREND"

        elif ema50 < ema200:

            trend = "DOWNTREND"

        # -----------------------------
        # Trend Strength
        # -----------------------------

        if adx > 30:

            regime = "TRENDING"

        elif adx < 20:

            regime = "RANGING"

        else:

            regime = "TRANSITION"

        # -----------------------------
        # Volatility
        # -----------------------------

        atr_mean = np.mean(closes) * 0.005

        if atr > atr_mean * 1.5:

            volatility = "HIGH"

        elif atr < atr_mean * 0.7:

            volatility = "LOW"

        else:

            volatility = "NORMAL"

        return {

            "trend": trend,

            "regime": regime,

            "volatility": volatility,

            "adx": adx,

            "atr": atr

        }