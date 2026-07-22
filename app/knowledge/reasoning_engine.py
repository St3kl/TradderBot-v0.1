class ReasoningEngine:
    """
    Uses learned relationships
    to recommend strategies.
    """

    def __init__(self, relationships):

        self.relationships = relationships

    def recommend(

        self,

        strategy,

        market_regime,

        volatility,

        session

    ):

        score = 0

        score += self.relationships.get_strength(

            strategy,

            "market_regime",

            market_regime

        )

        score += self.relationships.get_strength(

            strategy,

            "volatility",

            volatility

        )

        score += self.relationships.get_strength(

            strategy,

            "session",

            session

        )

        return {

            "strategy": strategy,

            "score": score

        }