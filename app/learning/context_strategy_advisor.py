class ContextStrategyAdvisor:
    """
    Selects the best strategy based on the
    current market context.
    """

    def recommend(

        self,

        market_statistics,

        regime,

        volatility

    ):

        key = f"{regime} | {volatility}"

        if key not in market_statistics:

            return {

                "strategy": None,

                "confidence": 0,

                "reason": "No historical context"

            }

        stats = market_statistics[key]

        return {

            "strategy": stats["best_strategy"],

            "confidence": stats["win_rate"],

            "reason": (

                f"{stats['best_strategy']} performs best "

                f"during {key}"

            )

        }