from app.quality.trade_quality import TradeQuality


class TradeQualityStage:

    def __init__(self):

        self.engine = TradeQuality()

    def run(self, session):

        print("Running Trade Quality Stage")

        session.trade_quality = self.engine.calculate(session)

        print("Trade Quality:", session.trade_quality)

        return session