class ResearchAgent:
    """
    Evaluates historical research quality
    of the selected strategy.
    """

    def evaluate(

        self,

        research

    ):

        score = 0

        reasons = []

        if research["win_rate"] >= 70:

            score += 30

            reasons.append("Strong win rate")

        if research["profit_factor"] >= 2:

            score += 30

            reasons.append("Strong profit factor")

        if research["research_score"] >= 90:

            score += 40

            reasons.append("Excellent research score")

        return {

            "agent": "Research",

            "score": score,

            "reasons": reasons

        }