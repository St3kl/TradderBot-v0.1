from app.ai.memory.memory_engine import MemoryEngine
from app.learning.strategy_statistics import StrategyStatistics
from app.learning.market_statistics import MarketStatistics
from app.learning.ai_statistics import AIStatistics
from app.learning.confidence_engine import ConfidenceEngine
from app.learning.recommendation_engine import RecommendationEngine
from app.learning.vector_updater import VectorUpdater


class LearningEngine:
    """
    Central orchestrator for the learning subsystem.

    Every completed trade passes through this engine.
    """

    def __init__(self):

        self.memory = MemoryEngine()

        self.strategy_statistics = StrategyStatistics()

        self.market_statistics = MarketStatistics()

        self.ai_statistics = AIStatistics()

        self.confidence_engine = ConfidenceEngine()

        self.recommendation_engine = RecommendationEngine()

        self.vector_updater = VectorUpdater()

    def learn(self, trade):

        print("\n========== LEARNING ENGINE ==========")

        self.memory.store(trade)

        self.strategy_statistics.update(trade)

        self.market_statistics.update(trade)

        self.ai_statistics.update(trade)

        self.confidence_engine.update(trade)

        self.vector_updater.update(trade)

        recommendation = self.recommendation_engine.generate()

        print("Learning Complete")

        return recommendation