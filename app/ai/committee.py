from app.ai.agents.bull_agent import BullAgent
from app.ai.agents.bear_agent import BearAgent
from app.ai.agents.risk_agent import RiskAgent
from app.ai.agents.execution_agent import ExecutionAgent
from app.ai.agents.research_agent import ResearchAgent
from app.ai.agents.chief_agent import ChiefAgent


class AICommittee:
    """
    Coordinates every AI agent and
    produces one final recommendation.
    """

    def __init__(self):

        self.bull = BullAgent()

        self.bear = BearAgent()

        self.risk = RiskAgent()

        self.execution = ExecutionAgent()

        self.research = ResearchAgent()

        self.chief = ChiefAgent()

    def evaluate(

        self,

        session,

        execution,

        portfolio,

        market,

        research

    ):

        reports = [

            self.bull.evaluate(session),

            self.bear.evaluate(session),

            self.risk.evaluate(

                execution,

                portfolio

            ),

            self.execution.evaluate(

                market

            ),

            self.research.evaluate(

                research

            )

        ]

        return self.chief.decide(

            reports

        )