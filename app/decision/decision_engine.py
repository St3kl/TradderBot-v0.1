from app.decision.confidence_engine import ConfidenceEngine


class DecisionEngine:
    """
    Final decision maker for TradderBot.
    """

    def __init__(self):

        self.confidence = ConfidenceEngine()

    def evaluate(self, session):

        confidence = self.confidence.calculate(session)

        session.decision = {

            "action": "WAIT",

            "reason": "Low Confidence",

            "confidence": confidence

        }

        # ------------------------------
        # LONG
        # ------------------------------

        if (

            confidence >= 75

            and

            session.validation["valid"]

            and

            session.trend["bullish"]

        ):

            session.decision = {

                "action": "LONG",

                "reason": "High Probability Long",

                "confidence": confidence

            }

        # ------------------------------
        # SHORT
        # ------------------------------

        elif (

            confidence >= 75

            and

            session.validation["valid"]

            and

            not session.trend["bullish"]

        ):

            session.decision = {

                "action": "SHORT",

                "reason": "High Probability Short",

                "confidence": confidence

            }

        return session