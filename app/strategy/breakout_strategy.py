from app.strategy.base_strategy import BaseStrategy


class BreakoutStrategy(BaseStrategy):

    name = "BREAKOUT"

    def evaluate(self, session):

        print("Evaluating Breakout Strategy")

        score = session.confluence["score"]

        structure = session.structure

        volume = session.volume

        alignment = session.alignment

        sweep = session.smart_money["liquidity_sweep"]

        # ---------------------------------
        # Require Break of Structure
        # ---------------------------------

        if structure["bos"]["type"] != "Bullish BOS":

            session.decision = {

                "action": "WAIT",

                "reason": "No Bullish BOS",

                "confidence": score

            }

            return session

        # ---------------------------------
        # Require strong volume
        # ---------------------------------

        if volume["score"] < 70:

            session.decision = {

                "action": "WAIT",

                "reason": "Weak breakout volume",

                "confidence": score

            }

            return session

        # ---------------------------------
        # Require Multi-Timeframe alignment
        # ---------------------------------

        if alignment < 3:

            session.decision = {

                "action": "WAIT",

                "reason": "Poor MTF alignment",

                "confidence": score

            }

            return session

        # ---------------------------------
        # Prefer liquidity sweep
        # ---------------------------------

        if not sweep["sell_side"]:

            session.decision = {

                "action": "WAIT",

                "reason": "No liquidity sweep",

                "confidence": score

            }

            return session

        # ---------------------------------
        # Minimum confluence
        # ---------------------------------

        if score < 75:

            session.decision = {

                "action": "WAIT",

                "reason": "Low confluence",

                "confidence": score

            }

            return session

        # ---------------------------------
        # Strategy Rules
        # ---------------------------------

        session.strategy_rules = {

            "minimum_rr": 2.5,

            "breakout_only": True,

            "require_bos": True,

            "require_volume": True,

            "require_mtf": True,

            "require_liquidity_sweep": True

        }

        return session