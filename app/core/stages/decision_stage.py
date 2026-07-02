from app.decision.engine import make_decision


class DecisionStage:

    def run(self, session):

        print("Running Decision Stage")

        session.decision = make_decision(
            session.confluence
        )

        return session