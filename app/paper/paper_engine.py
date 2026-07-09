from datetime import datetime

from app.database.services.trade_service import TradeService


class PaperTradingEngine:

    def __init__(self):

        self.trade_service = TradeService()

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

            "market_regime": session.market_regime.get("regime", "UNKNOWN"),

            "volatility": session.market_regime.get("volatility", "UNKNOWN"),

            "session_name": getattr(session, "session_name", "UNKNOWN"),

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

        self.trade_service.open_trade(trade)

        return trade