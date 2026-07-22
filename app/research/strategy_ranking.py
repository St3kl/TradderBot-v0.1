class StrategyRanking:
    """
    Ranks optimization results by score.
    """

    def rank(

        self,

        strategies,

        top=None

    ):

        ranked = sorted(

            strategies,

            key=lambda x: x["score"],

            reverse=True

        )

        if top:

            return ranked[:top]

        return ranked