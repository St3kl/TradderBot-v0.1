class CorrelationEngine:
    """
    Measures agreement between multiple markets.
    """

    def evaluate(self, session):

        timeframes = session.multi_timeframe

        bullish = 0
        bearish = 0

        for trend in timeframes.values():

            if trend == "Bullish":
                bullish += 1

            elif trend == "Bearish":
                bearish += 1

        total = bullish + bearish

        if total == 0:

            return {
                "alignment": "UNKNOWN",
                "score": 0,
            }

        agreement = max(bullish, bearish) / total

        if agreement >= 0.90:

            level = "VERY HIGH"

        elif agreement >= 0.75:

            level = "HIGH"

        elif agreement >= 0.60:

            level = "MEDIUM"

        else:

            level = "LOW"

        return {

            "alignment": level,

            "bullish": bullish,

            "bearish": bearish,

            "score": round(agreement * 100),

        }