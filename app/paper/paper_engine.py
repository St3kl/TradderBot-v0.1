from datetime import datetime

from app.database.repositories.trade_repository import TradeRepository


class PaperTradingEngine:

    def __init__(self):

        self.repo = TradeRepository()

    def open_trade(
        self,
        session,
        execution
    ):

        if not execution["execute"]:
            return None

        trade = {

            "symbol": session.symbol,

            "strategy": session.strategy,

            "direction": (
                "LONG"
                if session.bullish
                else "SHORT"
            ),

            "entry": session.trade["entry"],

            "stop_loss": session.trade["stop_loss"],

            "take_profit": session.trade["take_profit"],

            "position_size":
                execution["risk"]["position"]["position_size"],

            "risk_amount":
                execution["risk"]["position"]["risk_amount"],

            "confidence":
                session.decision["confidence"],

            "opened_at":
                datetime.utcnow().isoformat()

        }

        self.repo.create_trade(trade)

        return trade