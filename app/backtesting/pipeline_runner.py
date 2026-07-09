from app.core.registry import engine


class PipelineRunner:
    """
    Executes the complete TradderBot pipeline during backtesting.
    """

    def analyze(self, symbol):

        session = engine.analyze(symbol)

        return session