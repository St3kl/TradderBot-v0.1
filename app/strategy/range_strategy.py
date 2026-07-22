from app.strategy.base_strategy import BaseStrategy


class RangeStrategy(BaseStrategy):

    name = "RANGE"

    def evaluate(self, session):

        print("Evaluating Range Strategy")

        score = session.confluence["score"]

        trend = session.structure.trend

        liquidity = session.smart_money["liquidity"]

        # --------------------------------
        # Range strategies hate trends
        # --------------------------------

        if trend == "Bullish":

            session.decision = {

                "action": "WAIT",

                "reason": "Trending market",

                "confidence": score

            }

            return session

        # --------------------------------
        # Need liquidity pools
        # --------------------------------

        if (
            liquidity["equal_highs"] == 0
            and
            liquidity["equal_lows"] == 0
        ):

            session.decision = {

                "action": "WAIT",

                "reason": "No liquidity pools",

                "confidence": score

            }

            return session

        # --------------------------------
        # Minimum confluence
        # --------------------------------

        if score < 60:

            session.decision = {

                "action": "WAIT",

                "reason": "Low confluence",

                "confidence": score

            }

            return session

        # --------------------------------
        # Strategy Rules
        # --------------------------------

        session.strategy_rules = {

            "minimum_rr": 1.5,

            "allow_counter_trend": True,

            "require_liquidity": True,

            "mean_reversion": True

        }

        return session