from app.strategy.registry import StrategyRegistry

from app.strategy.trend_strategy import TrendStrategy
from app.strategy.range_strategy import RangeStrategy
from app.strategy.breakout_strategy import BreakoutStrategy
from app.strategy.reversal_strategy import ReversalStrategy


class StrategyEngine:

    def __init__(self):

        self.registry = StrategyRegistry()

        # Register all available strategies
        self.registry.register(TrendStrategy())
        self.registry.register(RangeStrategy())
        self.registry.register(BreakoutStrategy())
        self.registry.register(ReversalStrategy())

    # --------------------------------

    def evaluate(self, session):

        strategy = self.registry.get(session.strategy)

        if strategy is None:

            print(f"Unknown strategy: {session.strategy}")

            session.decision = {

                "action": "NO TRADE",
                "strategy": "NONE",
                "confidence": 0

            }

            return session

        return strategy.evaluate(session)