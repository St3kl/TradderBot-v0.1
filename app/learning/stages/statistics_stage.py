from app.learning.strategy_statistics import StrategyStatistics
from app.learning.market_statistics import MarketStatistics
from app.learning.ai_statistics import AIStatistics


class StatisticsStage:

    def __init__(self):

        self.strategy = StrategyStatistics()

        self.market = MarketStatistics()

        self.ai = AIStatistics()

    # ---------------------------------
    # Called after every trade
    # ---------------------------------

    def process(self, trade):

        self.strategy.update(trade)

        self.market.update(trade)

        self.ai.update(trade)

    # ---------------------------------
    # Used by reports
    # ---------------------------------

    def strategy_statistics(self):

        return self.strategy.summary()

    def market_statistics(self):

        return self.market.summary()

    def ai_statistics(self):

        return self.ai.summary()