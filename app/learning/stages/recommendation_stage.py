from app.learning.strategy_statistics import StrategyStatistics
from app.learning.market_statistics import MarketStatistics
from app.learning.ai_statistics import AIStatistics


class RecommendationStage:
    """
    Generates recommendations based on historical learning.
    """

    def __init__(self):

        self.strategy = StrategyStatistics()
        self.market = MarketStatistics()
        self.ai = AIStatistics()

    # --------------------------------------------------

    def process(self, trade):

        strategy_stats = self.strategy.summary()

        market_stats = self.market.summary()

        ai_stats = self.ai.summary()

        recommendation = {

    "strategy": self._best_strategy(strategy_stats),

    "market": self._best_market(market_stats),

    "confidence": self._best_confidence(ai_stats),

    "strategy_statistics": strategy_stats,

    "market_statistics": market_stats,

    "ai_statistics": ai_stats,

    "notes": self._generate_notes(

        strategy_stats,

        market_stats,

        ai_stats

    )

}

        return recommendation

    # --------------------------------------------------

    def _best_strategy(self, stats):

        if not stats:
            return None

        return max(
            stats.items(),
            key=lambda item: item[1]["win_rate"]
        )[0]

    # --------------------------------------------------

    def _best_market(self, stats):

        if not stats:
            return None

        return max(
            stats.items(),
            key=lambda item: item[1]["win_rate"]
        )[0]

    # --------------------------------------------------

    def _best_confidence(self, stats):

        if not stats:

            return None

        confidence = max(

            stats.items(),

            key=lambda item: item[1]["win_rate"]

        )[0]

    # Normalize every possible format

        if isinstance(confidence, str):

            confidence = confidence.replace("%", "")

            return int(float(confidence))

        return int(confidence)
    

    # --------------------------------------------------

    def _generate_notes(
        self,
        strategy_stats,
        market_stats,
        ai_stats
    ):

        notes = []

        best_strategy = self._best_strategy(strategy_stats)

        if best_strategy:

            notes.append(
                f"Prefer strategy: {best_strategy}"
            )

        best_market = self._best_market(market_stats)

        if best_market:

            notes.append(
                f"Best market condition: {best_market}"
            )

        best_confidence = self._best_confidence(ai_stats)

        if best_confidence:

            notes.append(
                f"Minimum preferred confidence: {best_confidence}"
            )

        return notes