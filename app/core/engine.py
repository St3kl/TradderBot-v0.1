from app.core.session import TradingSession
from app.core.pipeline import TradingPipeline
from app.core.engine import TradingEngine

engine = TradingEngine()


class TradingEngine:

    def __init__(self):

        self.pipeline = TradingPipeline()

    def analyze(self, symbol):

        session = TradingSession()

        session.symbol = symbol.upper()

        return self.pipeline.run(session)