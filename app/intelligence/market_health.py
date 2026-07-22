class MarketHealth:

    """
    Overall market quality score.
    """

    def evaluate(
        self,
        session,
    ):

        score = 100

        reasons = []

        # Weak Trend

        if session.trend["confidence"] < 60:

            score -= 20

            reasons.append("Weak Trend")

        # Weak Volume

        if session.volume["score"] < 20:

            score -= 20

            reasons.append("Weak Volume")

        # Low Confluence

        if session.confluence["score"] < 60:

            score -= 20

            reasons.append("Weak Confluence")

        # Poor Validation

        if session.validation["score"] < 70:

            score -= 20

            reasons.append("Trade Validation")

        # Range Market

        if session.structure.trend == "Range":

            score -= 10

            reasons.append("Range Market")

        # Unknown Regime

        if session.market_regime["regime"] == "UNKNOWN":

            score -= 10

            reasons.append("Unknown Regime")

        return {

            "score": max(score, 0),

            "reasons": reasons,

        }