class VolatilityMonitor:
    """
    Classifies current market volatility using ATR.
    """

    def evaluate(self, session):

        atr = session.indicators.get("atr", 0)
        price = session.indicators.get("price", 1)

        if price == 0:
            return {
                "level": "UNKNOWN",
                "score": 0,
            }

        volatility = (atr / price) * 100

        if volatility < 0.30:
            level = "LOW"
            score = 25

        elif volatility < 0.80:
            level = "NORMAL"
            score = 50

        elif volatility < 1.50:
            level = "HIGH"
            score = 75

        else:
            level = "EXTREME"
            score = 100

        return {
            "level": level,
            "score": score,
            "atr_percent": round(volatility, 3),
        }