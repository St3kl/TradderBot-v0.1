from app.strategy.base_strategy import BaseStrategy


class ReversalStrategy(BaseStrategy):

    name = "REVERSAL"

    def evaluate(self, session):

        print("Evaluating Reversal Strategy")

        score = session.confluence["score"]

        structure = session.structure

        smart_money = session.smart_money

        # ---------------------------------
        # Require CHoCH
        # ---------------------------------

        if not structure["choch"]:

            session.decision = {

                "action": "WAIT",

                "reason": "No CHoCH detected",

                "confidence": score

            }

            return session

        # ---------------------------------
        # Require Liquidity Sweep
        # ---------------------------------

        sweep = smart_money["liquidity_sweep"]

        if not (
            sweep["buy_side"]
            or
            sweep["sell_side"]
        ):

            session.decision = {

                "action": "WAIT",

                "reason": "No liquidity sweep",

                "confidence": score

            }

            return session

        # ---------------------------------
        # Require Premium/Discount Zone
        # ---------------------------------

        zone = smart_money["premium_discount"]["zone"]

        if zone not in ("Premium", "Discount"):

            session.decision = {

                "action": "WAIT",

                "reason": "No premium/discount edge",

                "confidence": score

            }

            return session

        # ---------------------------------
        # Require High Confluence
        # ---------------------------------

        if score < 80:

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

            "minimum_rr": 3.0,

            "reversal_only": True,

            "require_choch": True,

            "require_liquidity_sweep": True,

            "require_premium_discount": True

        }

        return session