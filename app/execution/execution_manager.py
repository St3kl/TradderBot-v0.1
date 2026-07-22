from datetime import datetime

from app.events.event_types import TradeExecuted

from app.execution.confirmation import ConfirmationEngine
from app.execution.entry_engine import EntryEngine
from app.risk.risk_manager import RiskManager


class ExecutionManager:
    """
    Coordinates the complete execution pipeline.

        Trading Session
              │
              ▼
        Entry Engine
              │
              ▼
      Confirmation Engine
              │
              ▼
        Risk Manager
              │
              ▼
       Publish Trade Event
    """

    def __init__(self, event_bus):

        self.bus = event_bus

        self.entry = EntryEngine()
        self.confirmation = ConfirmationEngine()
        self.risk = RiskManager()

    # ---------------------------------------------------------

    def evaluate(
        self,
        session,
        balance,
        risk_percent,
        open_positions
    ):

        # ---------------------------------------------
        # 1 Entry Validation
        # ---------------------------------------------

        entry = self.entry.evaluate(session)

        if not entry["execute"]:

            return {

                "execute": False,

                "reason": entry["reason"],

                "entry": entry,

                "confirmation": None,

                "risk": None

            }

        # ---------------------------------------------
        # 2 Confirmation Engine
        # ---------------------------------------------

        confirmation = self.confirmation.evaluate(session)

        if not confirmation["confirmed"]:

            return {

                "execute": False,

                "reason": "Confirmation failed",

                "entry": entry,

                "confirmation": confirmation,

                "risk": None

            }

        # ---------------------------------------------
        # 3 Risk Evaluation
        # ---------------------------------------------

        risk = self.risk.evaluate(

            balance=balance,

            risk_percent=risk_percent,

            trade=session.trade,

            open_positions=open_positions

        )

        if not risk["approved"]:

            return {

                "execute": False,

                "reason": "Risk rejected",

                "entry": entry,

                "confirmation": confirmation,

                "risk": risk

            }

        # ---------------------------------------------
        # Everything Approved
        # ---------------------------------------------

        result = {

            "execute": True,

            "entry": entry,

            "confirmation": confirmation,

            "risk": risk

        }

        # ---------------------------------------------
        # Publish Event
        # ---------------------------------------------

        event = TradeExecuted(

            symbol=session.symbol,

            side=session.decision["action"],

            entry=session.trade["entry"],

            stop_loss=session.trade["stop_loss"],

            take_profit=session.trade["take_profit"],

            confidence=session.decision["confidence"],

            strategy=session.strategy,

            regime=session.market_regime["regime"],

            volatility=session.market_regime["volatility"],

            timestamp=datetime.now()

        )

        self.bus.publish(event)

        return result

    # ---------------------------------------------------------

    def execute(
        self,
        session,
        balance,
        risk_percent,
        open_positions
    ):
        """
        Alias kept for compatibility.
        """

        return self.evaluate(

            session,

            balance,

            risk_percent,

            open_positions

        )