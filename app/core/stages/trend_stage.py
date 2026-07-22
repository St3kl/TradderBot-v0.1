class TrendStage:

    def run(self, session):

        print("Running Trend Stage")

        ema50 = session.indicators.get("ema50", 0)
        ema200 = session.indicators.get("ema200", 0)

        bullish = ema50 > ema200

        direction = "Bullish" if bullish else "Bearish"

        session.bullish = bullish

        strength = abs(ema50 - ema200)

        session.trend.update({

            "direction": direction,
            "bullish": bullish,
            "strength": round(strength, 4),
            "confidence": 70

        })

        # --------------------------------------------------
        # Initial Strategy Selection
        # --------------------------------------------------

        if strength > 50:

            session.strategy = "TREND"

        else:

            session.strategy = "RANGE"

        return session