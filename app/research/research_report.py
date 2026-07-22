class ResearchReport:
    """
    Builds a complete research report
    for a strategy.
    """

    def generate(

        self,

        strategy,

        metrics,

        score

    ):

        recommendation = "REVIEW"

        if score >= 90:

            recommendation = "LIVE READY"

        elif score >= 75:

            recommendation = "PAPER TRADE"

        return {

            "strategy": strategy,

            "metrics": metrics,

            "score": score,

            "recommendation": recommendation

        }