from app.database.repositories.trade_repository import TradeRepository
from app.portfolio.correlation_engine import CorrelationEngine


class GroupExposure:

    def __init__(self):

        self.repo = TradeRepository()

        self.correlation = CorrelationEngine()

    def exposure(self):

        trades = self.repo.get_open_trades()

        groups = {}

        for trade in trades:

            group = self.correlation.group(
                trade["symbol"]
            )

            groups[group] = groups.get(group, 0) + 1

        return groups