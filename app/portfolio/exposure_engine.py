from app.database.repositories.trade_repository import TradeRepository


class ExposureEngine:

    def __init__(self):

        self.repo = TradeRepository()

    def current_exposure(self):

        trades = self.repo.get_open_trades()

        total_risk = sum(
            trade["risk_amount"]
            for trade in trades
        )

        return {

            "open_trades": len(trades),

            "capital_at_risk": round(total_risk, 2)

        }