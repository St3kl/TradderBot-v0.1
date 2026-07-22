class StrategyReasoner:
    """
    Uses the Reasoning Engine to rank
    every available strategy.
    """

    def __init__(self, reasoning):

        self.reasoning = reasoning

    def select(

        self,

        strategies,

        market_regime,

        volatility,

        session

    ):

        results = []

        for strategy in strategies:

            result = self.reasoning.recommend(

                strategy,

                market_regime,

                volatility,

                session

            )

            results.append(result)

        results.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return results