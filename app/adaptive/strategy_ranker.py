from app.adaptive.strategy_score import StrategyScore


class StrategyRanker:

    def __init__(self):

        self.score = StrategyScore()

    def rank(self, statistics):

        ranking = []

        for strategy, stats in statistics.items():

            ranking.append({

                "strategy": strategy,

                "score": self.score.calculate(stats),

                "stats": stats

            })

        ranking.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return ranking