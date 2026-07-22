from app.database.repositories.trade_repository import TradeRepository


class MetricsEngine:

    def __init__(self):

        self.repo = TradeRepository()

    def build(self):

        trades = self.repo.get_closed_trades()

        if not trades:

            return {}

        wins = []
        losses = []

        for trade in trades:

            pnl = trade["pnl"] or 0

            if pnl > 0:

                wins.append(pnl)

            elif pnl < 0:

                losses.append(abs(pnl))

        total = len(trades)

        win_rate = len(wins) / total if total else 0

        loss_rate = len(losses) / total if total else 0

        avg_win = sum(wins) / len(wins) if wins else 0

        avg_loss = sum(losses) / len(losses) if losses else 0

        expectancy = (

            win_rate * avg_win

            -

            loss_rate * avg_loss

        )

        if avg_loss == 0:

            profit_factor = float("inf")

        else:

            profit_factor = (

                sum(wins)

                /

                sum(losses)

            )

        return {

            "average_win": round(avg_win, 2),

            "average_loss": round(avg_loss, 2),

            "expectancy": round(expectancy, 2),

            "profit_factor": round(profit_factor, 2)
            if profit_factor != float("inf")
            else "Infinity"

        }