from app.portfolio.exposure_engine import ExposureEngine
from app.portfolio.group_exposure import GroupExposure
from app.portfolio.risk_limits import (
    MAX_OPEN_TRADES,
    MAX_CAPITAL_AT_RISK,
)


class PortfolioGuard:

    def __init__(self):

        self.exposure = ExposureEngine()
        self.groups = GroupExposure()

    def can_open_trade(self, symbol=None):

        stats = self.exposure.current_exposure()

        # Maximum number of open trades
        if stats["open_trades"] >= MAX_OPEN_TRADES:
            return False

        # Maximum capital at risk
        if stats["capital_at_risk"] >= MAX_CAPITAL_AT_RISK:
            return False

        # Correlation exposure
        if symbol:

            group_exposure = self.groups.exposure()

            correlation_group = self.groups.correlation.group(symbol)

            if group_exposure.get(correlation_group, 0) >= 3:
                return False

        return True