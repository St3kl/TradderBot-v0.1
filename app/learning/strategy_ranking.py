class StrategyRanking:
    """
    Ranks strategies based on historical performance.
    """

    def rank(self, statistics):

        ranking = []

        for strategy, stats in statistics.items():

            ranking.append({

                "strategy": strategy,

                "win_rate": stats["win_rate"],

                "trades": stats["total"]

            })

        ranking.sort(

            key=lambda x: (

                x["win_rate"],

                x["trades"]

            ),

            reverse=True

        )

        return ranking