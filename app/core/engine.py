from app.core.pipeline_builder import PipelineBuilder
from app.core.session import TradingSession


class TradingEngine:

    def __init__(self, adaptive_config):

        self.config = adaptive_config

        self.pipeline = PipelineBuilder.build()

    def analyze(self, context, balance=10000):

        session = TradingSession()

        session.symbol = context.symbol
        session.replay = context
        session.balance = balance

        session = self.pipeline.run(session)
        

        ...

        # ---------------------------------
        # Apply Adaptive Learning
        # ---------------------------------

        config = self.config.get()

        if (
            session.decision["confidence"]
            < config["minimum_confidence"]
        ):

            session.decision["action"] = "WAIT"

        return session