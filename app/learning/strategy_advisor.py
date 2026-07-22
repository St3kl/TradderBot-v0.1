class StrategyAdvisor:
    """
    Uses historical rankings to recommend the best strategy.
    """

    def recommend(self, ranking):

        if not ranking:

            return {

                "strategy": None,

                "confidence": 0,

                "reason": "No historical data"

            }

        best = ranking[0]

        confidence = min(

            95,

            round(

                best["win_rate"] * 0.9 +

                best["trades"] * 0.1,

                2

            )

        )

        return {

            "strategy": best["strategy"],

            "confidence": confidence,

            "reason": f"{best['strategy']} has the highest historical win rate ({best['win_rate']}%)"

        }