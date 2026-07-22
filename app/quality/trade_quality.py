class TradeQuality:

    """
    Calculates a final quality score for every trade.

    This is the final score before execution.
    """

    def calculate(self, session):

        confluence = session.confluence.get("score", 0)

        validation = session.validation.get("score", 0)

        confidence = session.decision.get("confidence", 0)

        market = getattr(session, "market_health", {"score": 50}).get("score", 50)

        volatility = getattr(session, "volatility", {"score": 50}).get("score", 50)

        correlation = getattr(session, "correlation", {"score": 50}).get("score", 50)
        
        score = (
            confluence * 0.25
            + validation * 0.20
            + confidence * 0.20
            + market * 0.15
            + volatility * 0.10
            + correlation * 0.10
        )

        score = round(score, 2)

        if score >= 90:
            grade = "A+"

        elif score >= 80:
            grade = "A"

        elif score >= 70:
            grade = "B"

        elif score >= 60:
            grade = "C"

        else:
            grade = "D"

        return {

            "score": score,

            "grade": grade

        }