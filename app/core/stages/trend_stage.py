class TrendStage:

    def run(self, session):

        print("Running Trend Stage")

        session.bullish = (
            session.indicators["ema50"]
            >
            session.indicators["ema200"]
        )

        return session