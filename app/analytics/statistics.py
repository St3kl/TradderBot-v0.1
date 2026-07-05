from app.database.repositories.trade_repository import TradeRepository


class StatisticsEngine:

    def __init__(self):

        self.repo = TradeRepository()

    def total_trades(self):

        return len(

            self.repo.get_all_trades()

        )

    def open_trades(self):

        return len(

            self.repo.get_open_trades()

        )

    def closed_trades(self):

        return len(

            self.repo.get_closed_trades()

        )

    def wins(self):

        return len(

            self.repo.get_winning_trades()

        )

    def losses(self):

        return len(

            self.repo.get_losing_trades()

        )

    def summary(self):

        return {

            "total_trades": self.total_trades(),

            "open_trades": self.open_trades(),

            "closed_trades": self.closed_trades(),

            "wins": self.wins(),

            "losses": self.losses()

        }