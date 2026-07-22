import uuid
from datetime import datetime

from app.database.services.trade_service import TradeService


class PaperTradingEngine:
    """
    Simulates a broker.

    Responsible for:

        - Opening trades
        - Closing trades
        - Recording execution
        - Simulating commissions
        - Simulating slippage
    """

    COMMISSION = 0.0004      # 0.04%
    SLIPPAGE = 0.0002        # 0.02%

    def __init__(self):

        self.trade_service = TradeService()

    # =====================================================
    # OPEN TRADE
    # =====================================================

    def open_trade(self, session, execution):

        if not execution["execute"]:

            return None

        trade = {

            "id": str(uuid.uuid4()),

            "status": "OPEN",

            "symbol": session.symbol,

            "strategy": session.strategy,

            "market_regime":
                session.market_regime["regime"],

            "volatility":
                session.market_regime["volatility"],

            "session_name":
                getattr(session, "session_name", "UNKNOWN"),

            "direction":

                "LONG"

                if session.bullish

                else "SHORT",

            "entry":
                session.trade["entry"],

            "stop_loss":
                session.trade["stop_loss"],

            "take_profit":
                session.trade["take_profit"],

            "position_size":

                execution["risk"]["position"]["position_size"],

            "risk_amount":

                execution["risk"]["position"]["risk_amount"],

            "confidence":
                session.decision["confidence"],

            "commission": 0,

            "slippage": 0,

            "opened_at":
                datetime.utcnow().isoformat()

        }

        self.trade_service.open_trade(trade)

        return trade

    # =====================================================
    # CLOSE TRADE
    # =====================================================

    def close_trade(

        self,

        trade,

        exit_price,

        result

    ):

        entry = trade["entry"]

        direction = trade["direction"]

        # ----------------------------------------

        if direction == "LONG":

            gross = exit_price - entry

        else:

            gross = entry - exit_price

        # ----------------------------------------
        # Simulated Costs
        # ----------------------------------------

        commission = abs(entry) * self.COMMISSION

        slippage = abs(entry) * self.SLIPPAGE

        pnl = gross - commission - slippage

        # ----------------------------------------

        trade["status"] = "CLOSED"

        trade["exit_price"] = exit_price

        trade["commission"] = commission

        trade["slippage"] = slippage

        trade["pnl"] = pnl

        trade["gross_pnl"] = gross

        trade["result"] = result

        trade["closed_at"] = datetime.utcnow().isoformat()

        # ----------------------------------------
        # Duration
        # ----------------------------------------

        try:

            opened = datetime.fromisoformat(

                trade["opened_at"]

            )

            closed = datetime.fromisoformat(

                trade["closed_at"]

            )

            trade["duration"] = (

                closed - opened

            ).total_seconds()

        except Exception:

            trade["duration"] = 0

        # ----------------------------------------

        self.trade_service.close_trade(

            trade["id"],

            exit_price,

            pnl,

            result

        )

        return trade

    # =====================================================
    # CANCEL
    # =====================================================

    def cancel_trade(self, trade):

        trade["status"] = "CANCELLED"

        trade["closed_at"] = datetime.utcnow().isoformat()

        return trade