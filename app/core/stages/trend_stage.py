class TrendStage:

    def run(self, session):

        print("Running Trend Stage")

        ema50 = session.indicators.get("ema50", 0)
        ema200 = session.indicators.get("ema200", 0)

        bullish = ema50 > ema200
        direction = "Bullish" if bullish else "Bearish"

        # Backward compatibility
        session.bullish = bullish

        # Update the trend section of the session
        session.trend.update({
            "direction": direction,
            "bullish": bullish,
            "strength": round(abs(ema50 - ema200), 4),
            "confidence": 70
        })

        return session