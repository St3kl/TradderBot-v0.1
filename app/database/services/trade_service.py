from app.database.repositories.trade_repository import TradeRepository


class TradeService:
    """
    Business layer for trade persistence.

    Engines should communicate with this service
    instead of repositories directly.
    """

    def __init__(self):

        self.repo = TradeRepository()

    def open_trade(self, trade):

        self.repo.create_trade(trade)

    def close_trade(
        self,
        trade_id,
        exit_price,
        pnl,
        result
    ):

        self.repo.close_trade(
            trade_id,
            exit_price,
            pnl,
            result
        )

    def get_open_trades(self):

        return self.repo.get_open_trades()

    def get_closed_trades(self):

        return self.repo.get_closed_trades()

    def get_all_trades(self):

        return self.repo.get_all_trades()