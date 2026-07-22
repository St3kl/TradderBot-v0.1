from app.adaptive.strategy_ranker import StrategyRanker
from app.adaptive.strategy_selector import StrategySelector


class AdaptiveEngine:

    def __init__(self):

        self.ranker = StrategyRanker()

        self.selector = StrategySelector()

    def evaluate(self, strategy_statistics):

        ranking = self.ranker.rank(

            strategy_statistics

        )

        best = self.selector.choose(

            ranking

        )

        return {

            "best": best,

            "ranking": ranking

        }