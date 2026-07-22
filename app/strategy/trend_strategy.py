from app.strategy.base_strategy import BaseStrategy


class TrendStrategy(BaseStrategy):

    name = "TREND"

    def evaluate(self, session):

        print("Evaluating Trend Strategy")

        score = session.confluence["score"]

        trend = session.structure["trend"]

        bullish = session.bullish

        # -----------------------------
        # Must follow trend
        # -----------------------------

        if not bullish:

            session.decision = {

                "action": "WAIT",

                "reason": "Trend is bearish",

                "confidence": 0

            }

            return session

        # -----------------------------
        # Must have bullish structure
        # -----------------------------

        if trend != "Bullish":

            session.decision = {

                "action": "WAIT",

                "reason": "Market structure not bullish",

                "confidence": score

            }

            return session

        # -----------------------------
        # Minimum confluence
        # -----------------------------

        if score < 70:

            session.decision = {

                "action": "WAIT",

                "reason": "Low confluence",

                "confidence": score

            }

            return session

        # -----------------------------
        # Strategy Rules
        # -----------------------------

        session.strategy_rules = {

            "minimum_rr": 2.0,

            "allow_counter_trend": False,

            "require_bos": True,

            "require_discount": True

        }

        return session