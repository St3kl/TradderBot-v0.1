from app.strategy.base_strategy import BaseStrategy


class BreakoutStrategy(BaseStrategy):

    name = "BREAKOUT"

    def execute(self, session):

        print("Executing Breakout Strategy")

        session.strategy_rules = {

            "breakout_only": True,

            "minimum_rr": 2.5

        }

        return session