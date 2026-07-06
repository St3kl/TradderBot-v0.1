from app.strategy.base_strategy import BaseStrategy


class ReversalStrategy(BaseStrategy):

    name = "REVERSAL"

    def execute(self, session):

        print("Executing Reversal Strategy")

        session.strategy_rules = {

            "reversal_only": True,

            "minimum_rr": 3.0

        }

        return session