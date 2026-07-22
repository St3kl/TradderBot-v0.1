from app.ai_coach.trade_reviewer import TradeReviewer
from app.ai_coach.strategy_advisor import StrategyAdvisor
from app.ai_coach.market_advisor import MarketAdvisor


class AICoach:

    def __init__(self):

        self.trade = TradeReviewer()

        self.strategy = StrategyAdvisor()

        self.market = MarketAdvisor()

    def review(

        self,

        trades,

        learning

    ):

        return {

            "trade": self.trade.review(

                trades

            ),

            "strategy": self.strategy.review(

                learning["strategy"]

            ),

            "market": self.market.review(

                learning["market"]

            )

        }