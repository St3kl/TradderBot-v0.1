from app.database.repositories.trade_repository import TradeRepository


class PerformanceEngine:

    def __init__(self):

        self.repo = TradeRepository()

    def build(self):

        trades = self.repo.get_closed_trades()

        if not trades:

            return {

                "total": 0,

                "wins": 0,

                "losses": 0,

                "win_rate": 0,

                "average_pnl": 0

            }

        wins = [
            t for t in trades
            if t["result"] == "WIN"
        ]

        losses = [
            t for t in trades
            if t["result"] == "LOSS"
        ]

        total = len(trades)

        total_pnl = sum(t["pnl"] for t in trades)

        return {

            "total": total,

            "wins": len(wins),

            "losses": len(losses),

            "win_rate": round(
                len(wins) / total * 100,
                2
            ),

            "average_pnl": round(
                total_pnl / total,
                2
            )

        }