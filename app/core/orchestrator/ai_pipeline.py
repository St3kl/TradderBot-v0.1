from app.orchestrator.pipeline_context import PipelineContext

from app.ai.decision_brain import DecisionBrain


class AIPipeline:
    """
    Coordinates every intelligent subsystem.
    """

    def __init__(

        self,

        market_engine,

        execution_manager,

        paper_engine,

        learning_engine,

        portfolio_manager

    ):

        self.market = market_engine

        self.execution = execution_manager

        self.paper = paper_engine

        self.learning = learning_engine

        self.portfolio = portfolio_manager

        self.brain = DecisionBrain()

    def process(

        self,

        symbol

    ):

        ctx = PipelineContext()

        ctx.symbol = symbol

        # 1 Market Analysis

        ctx.session = self.market.analyze(symbol)

        # 2 Research

        ctx.research = {

            "win_rate":74,

            "profit_factor":2.4,

            "research_score":94

        }

        # 3 Portfolio

        ctx.portfolio = {

            "drawdown":2,

            "exposure":20

        }

        # 4 Market Conditions

        ctx.market = {

            "spread":0.05,

            "slippage":0.04,

            "liquidity":"HIGH"

        }

        # 5 Execution Analysis

        ctx.execution = self.execution.evaluate(

            session=ctx.session,

            balance=10000,

            risk_percent=1,

            open_positions=[]

        )

        # 6 AI Committee

        ctx.decision = self.brain.decide(

            ctx.session,

            ctx.execution,

            ctx.portfolio,

            ctx.market,

            ctx.research

        )

        return ctx