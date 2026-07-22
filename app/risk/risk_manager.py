from app.risk.drawdown_guard import DrawdownGuard
from app.risk.daily_loss_guard import DailyLossGuard
from app.risk.exposure_manager import ExposureManager
from app.risk.portfolio_heat import PortfolioHeat
from app.risk.trading_window_guard import TradingWindowGuard


class RiskManager:
    """
    Centralized institutional risk engine.
    """

    def __init__(self):

        self.drawdown = DrawdownGuard()
        self.daily = DailyLossGuard()
        self.exposure = ExposureManager()
        self.heat = PortfolioHeat()
        self.window = TradingWindowGuard()

    def evaluate(self, session, portfolio, open_positions):

        checks = []

        # -----------------------
        # Drawdown
        # -----------------------

        checks.append(

            self.drawdown.evaluate(portfolio)

        )

        # -----------------------
        # Daily Loss
        # -----------------------

        checks.append(

            self.daily.evaluate(portfolio)

        )

        # -----------------------
        # Exposure
        # -----------------------

        checks.append(

            self.exposure.evaluate(open_positions)

        )

        # -----------------------
        # Portfolio Heat
        # -----------------------

        checks.append(

            self.heat.evaluate(open_positions)

        )

        # -----------------------
        # Trading Window
        # -----------------------

        checks.append(

            self.window.evaluate(session)

        )

        reasons = []

        for result in checks:

            if not result["allowed"]:

                reason = result.get("reason")

                if reason:

                    reasons.append(reason)

                reasons.extend(result.get("reasons", []))

        return {

            "allowed": len(reasons) == 0,

            "reasons": reasons

        }