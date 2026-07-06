from app.strategy.base_strategy import BaseStrategy


class TrendStrategy(BaseStrategy):

    name = "TREND"

    def execute(self, session):

        print("Executing Trend Strategy")

        session.strategy_rules = {

            "allow_trend_following": True,

            "allow_counter_trend": False,

            "minimum_rr": 2.0

        }

        return session