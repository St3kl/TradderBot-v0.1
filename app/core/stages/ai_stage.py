from app.ai.engine import AIEngine
from app.ai.health import AIHealth


class AIStage:

    def __init__(self):

        self.ai = AIEngine()
        self.health = AIHealth()

    def run(self, session):

        print("Running AI Stage")

        if self.health.check():

            try:

                # session.ai_report = self.ai.analyze(session)
                report = self.ai.analyze(session)

                session.ai["report"] = report

                # compatibility
                session.ai_report = report

            except Exception as e:

                print("AI ERROR:", e)

                session.ai_report = self.offline_report()

        else:

            session.ai_report = self.offline_report()

        return session

    def offline_report(self):

        return {

            "market_summary": "AI server offline",

            "trade_validation": "",

            "risk_assessment": "",

            "institutional_opinion": "",

            "recommendation": "WAIT"

        }