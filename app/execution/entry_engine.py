class EntryEngine:
    """
    Entry Validation Engine

    Validates that a trade setup is complete before
    allowing the execution pipeline to continue.
    """

    def evaluate(self, session):

        decision = session.decision
        trade = session.trade

        # ----------------------------------------
        # Trading Engine Decision
        # ----------------------------------------

        if decision["action"] in ("WAIT", "NO TRADE"):

            return {

                "execute": False,

                "reason": "Trading engine rejected setup."

            }

        # ----------------------------------------
        # Entry
        # ----------------------------------------

        if trade["entry"] is None:

            return {

                "execute": False,

                "reason": "Missing entry price."

            }

        # ----------------------------------------
        # Stop Loss
        # ----------------------------------------

        if trade["stop_loss"] is None:

            return {

                "execute": False,

                "reason": "Missing stop loss."

            }

        # ----------------------------------------
        # Take Profit
        # ----------------------------------------

        if trade["take_profit"] is None:

            return {

                "execute": False,

                "reason": "Missing take profit."

            }

        # ----------------------------------------
        # Risk / Reward
        # ----------------------------------------

        rr = trade.get("risk_reward", 0)

        if rr < 1.5:

            return {

                "execute": False,

                "reason": f"Risk/Reward too low ({rr})."

            }

        # ----------------------------------------
        # Confidence
        # ----------------------------------------

        confidence = decision.get("confidence", 0)

        if confidence < 60:

            return {

                "execute": False,

                "reason": f"Confidence too low ({confidence}%)."

            }

        # ----------------------------------------
        # Validation Stage
        # ----------------------------------------

        if not session.validation.get("valid", True):

            return {

                "execute": False,

                "reason": "Validation stage rejected trade."

            }

        # ----------------------------------------
        # Checklist
        # ----------------------------------------

        if len(session.checklist.get("failed", [])) > 0:

            return {

                "execute": False,

                "reason": "Checklist failed."

            }

        # ----------------------------------------
        # Approved
        # ----------------------------------------

        return {

            "execute": True,

            "entry": trade["entry"],

            "stop_loss": trade["stop_loss"],

            "take_profit": trade["take_profit"],

            "risk_reward": rr,

            "confidence": confidence

        }