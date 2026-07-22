from app.learning.stages.memory_stage import MemoryStage
from app.learning.stages.statistics_stage import StatisticsStage
from app.learning.stages.recommendation_stage import RecommendationStage
from app.learning.stages.optimization_stage import OptimizationStage

from app.logger.logger import Logger

logger = Logger.get("LearningEngine")


class LearningEngine:

    def __init__(self, adaptive_config):

        self.config = adaptive_config

        self.memory = MemoryStage()

        self.statistics_stage = StatisticsStage()

        self.recommendation = RecommendationStage()

        self.optimization = OptimizationStage()

    # ---------------------------------

    def learn(self, trade):

        print()
        print("========== LEARNING ==========")

        # Memory

        self.memory.process(trade)

        # Statistics

        self.statistics_stage.process(trade)

        # Recommendation

        recommendation = self.recommendation.process(
            trade
        )

        # Optimization

        optimized = self.optimization.process(
            recommendation
        )

        # Store latest optimized parameters

        self.config.update(optimized)

        logger.info("Learning Complete")

        return optimized

    # ---------------------------------
    # Statistics used by Backtest Report
    # ---------------------------------

    def statistics(self):

        return {

            "strategy":
                self.statistics_stage.strategy_statistics(),

            "market":
                self.statistics_stage.market_statistics(),

            "ai":
                self.statistics_stage.ai_statistics()

        }