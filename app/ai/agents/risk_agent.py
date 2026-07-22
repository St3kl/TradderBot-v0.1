class RiskAgent:
    """
    Evaluates trading risk.

    Can recommend reducing confidence
    or blocking a trade.
    """

    def evaluate(

        self,

        execution,

        portfolio

    ):

        score = 100

        reasons = []

        # Daily Drawdown

        if portfolio["drawdown"] > 10:

            score -= 40

            reasons.append(

                "High drawdown"

            )

        # Exposure

        if portfolio["exposure"] > 50:

            score -= 30

            reasons.append(

                "High exposure"

            )

        # Position Risk

        if execution["risk"]["position"]["risk_amount"] > 200:

            score -= 20

            reasons.append(

                "Large position risk"

            )

        return {

            "agent": "Risk",

            "score": max(score, 0),

            "reasons": reasons

        }