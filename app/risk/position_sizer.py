from math import floor


class PositionSizer:
    """
    Calculates position size based on account risk.
    """

    def calculate(
        self,
        balance,
        risk_percent,
        entry,
        stop_loss,
    ):
        risk_amount = balance * (risk_percent / 100)

        stop_distance = abs(entry - stop_loss)

        if stop_distance <= 0:
            return {
                "position_size": 0,
                "risk_amount": risk_amount,
            }

        position_size = risk_amount / stop_distance

        return {
            "position_size": round(position_size, 6),
            "risk_amount": round(risk_amount, 2),
        }