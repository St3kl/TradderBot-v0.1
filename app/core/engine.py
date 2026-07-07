from app.core.pipeline_builder import PipelineBuilder
from app.core.session import TradingSession


class TradingEngine:

    def __init__(self):

        self.pipeline = PipelineBuilder.build()

    def analyze(self, symbol):

        session = TradingSession()

        session.symbol = symbol.upper()

        return self.pipeline.run(session)