from app.market.market_engine import MarketEngine


class MarketPipeline:
    """
    Executes the complete market analysis.

    This class orchestrates every market-related engine
    before strategy selection.
    """

    def __init__(self):

        self.market = MarketEngine()

    # -----------------------------------

    def run(self, session):

        self.market.analyze(session)

        return session