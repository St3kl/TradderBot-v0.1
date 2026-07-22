from app.ai.committee import AICommittee


class DecisionBrain:
    """
    High-level AI orchestrator.

    Delegates analysis to the AI Committee.
    """

    def __init__(self):

        self.committee = AICommittee()

    def decide(

        self,

        session,

        execution,

        portfolio,

        market,

        research

    ):

        return self.committee.evaluate(

            session,

            execution,

            portfolio,

            market,

            research

        )