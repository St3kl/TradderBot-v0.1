from app.risk.position_sizing import calculate_position_size
from app.risk.portfolio import calculate_portfolio_risk
from app.risk.exposure import analyze_exposure


class RiskManager:

    def evaluate(
        self,
        balance,
        risk_percent,
        trade,
        open_positions
    ):

        position = calculate_position_size(

            balance=balance,

            risk_percent=risk_percent,

            entry=trade["entry"],

            stop_loss=trade["stop_loss"]

        )

        portfolio = calculate_portfolio_risk(
            open_positions
        )

        exposure = analyze_exposure(
            open_positions
        )

        approved = True

        reasons = []

        # -----------------------------
        # Portfolio Risk Limit
        # -----------------------------

        if portfolio["total_risk"] >= balance * 0.05:

            approved = False

            reasons.append(
                "Maximum portfolio risk exceeded."
            )

        # -----------------------------
        # Net Exposure
        # -----------------------------

        if abs(exposure["net_exposure"]) >= balance * 0.03:

            reasons.append(
                "High directional exposure."
            )

        return {

            "approved": approved,

            "position": position,

            "portfolio": portfolio,

            "exposure": exposure,

            "reasons": reasons

        }