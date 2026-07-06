from app.strategy.trend_strategy import TrendStrategy
from app.strategy.range_strategy import RangeStrategy
from app.strategy.breakout_strategy import BreakoutStrategy
from app.strategy.reversal_strategy import ReversalStrategy


class StrategyEngine:

    def __init__(self):

        self.strategies = {

            "TREND": TrendStrategy(),

            "RANGE": RangeStrategy(),

            "BREAKOUT": BreakoutStrategy(),

            "REVERSAL": ReversalStrategy()

        }

    def execute(self, session):

        strategy = self.strategies.get(session.strategy)

        if strategy is None:

            return session

        return strategy.execute(session)