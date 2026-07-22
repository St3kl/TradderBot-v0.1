from app.database.repositories.trade_repository import TradeRepository


class StatisticsEngine:

    def __init__(self):

        self.repo = TradeRepository()

    def build(self):

        trades = self.repo.get_closed_trades()

        total = len(trades)

        wins = 0
        losses = 0

        gross_profit = 0
        gross_loss = 0

        for trade in trades:

            pnl = trade["pnl"] or 0

            if pnl > 0:

                wins += 1
                gross_profit += pnl

            elif pnl < 0:

                losses += 1
                gross_loss += abs(pnl)

        if total > 0:

            win_rate = (wins / total) * 100

        else:

            win_rate = 0

        net_profit = gross_profit - gross_loss

        return {

            "total_trades": total,

            "wins": wins,

            "losses": losses,

            "win_rate": round(win_rate, 2),

            "gross_profit": round(gross_profit, 2),

            "gross_loss": round(gross_loss, 2),

            "net_profit": round(net_profit, 2)

        }