from app.strategy.base_strategy import BaseStrategy


class RangeStrategy(BaseStrategy):

    name = "RANGE"

    def execute(self, session):

        print("Executing Range Strategy")

        session.strategy_rules = {

            "allow_trend_following": False,

            "allow_counter_trend": True,

            "minimum_rr": 1.5

        }

        return session