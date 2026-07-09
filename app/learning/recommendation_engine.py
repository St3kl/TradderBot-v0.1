from app.learning.strategy_statistics import StrategyStatistics
from app.learning.market_statistics import MarketStatistics


class RecommendationEngine:
    """
    Generates recommendations based on historical performance.
    """

    def __init__(self):

        self.strategy_stats = StrategyStatistics()
        self.market_stats = MarketStatistics()

    def recommend(
        self,
        strategy,
        regime,
        volatility
    ):

        strategies = self.strategy_stats.summary()

        markets = self.market_stats.summary()

        strategy_info = strategies.get(strategy)

        market_key = f"{regime} | {volatility}"

        market_info = markets.get(market_key)

        recommendation = {

            "strategy": strategy,

            "confidence": 50,

            "reason": []

        }

        # ----------------------------
        # Strategy Learning
        # ----------------------------

        if strategy_info:

            recommendation["confidence"] += int(

                strategy_info["win_rate"] / 10

            )

            recommendation["reason"].append(

                f"Strategy historical win rate: "
                f"{strategy_info['win_rate']}%"

            )

        # ----------------------------
        # Market Learning
        # ----------------------------

        if market_info:

            recommendation["confidence"] += int(

                market_info["win_rate"] / 20

            )

            recommendation["reason"].append(

                f"Market historical win rate: "
                f"{market_info['win_rate']}%"

            )

        recommendation["confidence"] = min(

            recommendation["confidence"],

            100

        )

        return recommendation