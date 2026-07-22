from app.checklist.institutional_checklist import (
    build_checklist
)
# from app.analysis.checklist.institutional_checklist import ...

class ChecklistStage:

    def run(self, session):

        print("Running Checklist Stage")

        session.checklist = build_checklist(
            bullish=session.bullish,
            structure=session.structure,
            smart_money=session.smart_money,
            volume=session.volume,
            trade=session.trade
        )

        return session