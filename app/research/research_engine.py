from app.optimization.grid_search import GridSearch
from app.optimization.optimization_runner import OptimizationRunner

from app.research.strategy_ranking import StrategyRanking
from app.research.research_report import ResearchReport


class ResearchEngine:
    """
    Central orchestrator for the
    quantitative research pipeline.
    """

    def __init__(self):

        self.grid = GridSearch()

        self.runner = OptimizationRunner()

        self.ranking = StrategyRanking()

        self.report = ResearchReport()

    def run(

        self,

        parameters,

        evaluator

    ):

        print()

        print("=" * 60)

        print("RESEARCH ENGINE")

        print("=" * 60)

        print()

        parameter_sets = self.grid.generate(

            parameters

        )

        results = self.runner.run(

            parameter_sets,

            evaluator

        )

        ranked = self.ranking.rank(results)

        return ranked