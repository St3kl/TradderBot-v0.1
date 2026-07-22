class PipelineRunner:
    """
    Executes the complete TradderBot pipeline during backtesting.
    """

    def __init__(self, trading_engine):

        self.engine = trading_engine

    def analyze(self, context, balance,):

        return self.engine.analyze(context, balance=balance,)