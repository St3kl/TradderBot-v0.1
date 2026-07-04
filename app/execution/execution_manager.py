from app.execution.confirmation import ConfirmationEngine
from app.execution.entry_engine import EntryEngine
from app.risk.risk_manager import RiskManager


class ExecutionManager:

    def __init__(self):

        self.confirmation = ConfirmationEngine()
        self.entry = EntryEngine()
        self.risk = RiskManager()

    def evaluate(
        self,
        session,
        balance,
        risk_percent,
        open_positions
    ):

        confirmation = self.confirmation.evaluate(session)

        risk = self.risk.evaluate(
            balance=balance,
            risk_percent=risk_percent,
            trade=session.trade,
            open_positions=open_positions
        )

        entry = self.entry.evaluate(session)

        execute = (

            entry["execute"]

            and

            risk["approved"]

            and

            confirmation["confirmed"]

        )

        return {

            "execute": execute,

            "entry": entry,

            "risk": risk,

            "confirmation": confirmation

        }