from datetime import datetime


class TradeFactory:
    """
    Creates fake trades for tests.
    """

    @staticmethod
    def create(**overrides):

        trade = {

            "symbol": "BTCUSDT",

            "strategy": "DEFAULT",

            "market_regime": "TRANSITION",

            "volatility": "NORMAL",

            "session_name": "UNKNOWN",

            "direction": "LONG",

            "entry": 62000,

            "stop_loss": 61500,

            "take_profit": 63000,

            "position_size": 0.20,

            "risk_amount": 100,

            "confidence": 65,

            "opened_at": datetime.utcnow().isoformat(),

            "status": "OPEN",

            "result": "WIN"

        }

        trade.update(overrides)

        return trade