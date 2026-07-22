from app.container.application_container import ApplicationContainer
from app.live.live_engine import LiveEngine


class Application:
    """
    TradderBot Application Bootstrap

    Creates the dependency container and exposes
    the main application services.
    """

    def __init__(self):

        self.container = ApplicationContainer()
        self.container.register_subscribers()
        self.live = LiveEngine()

    @property
    def backtest(self):

        return self.container.backtest()

    @property
    def trading_engine(self):

        return self.container.trading_engine()

    @property
    def execution(self):

        return self.container.execution()

    @property
    def learning(self):

        return self.container.learning()