class PortfolioHeat:

    """
    Controls total portfolio risk.
    """

    def __init__(self):

        self.max_heat = 5.0  # percent

    def evaluate(self, open_positions):

        total_heat = sum(
            position.get("risk_percent", 0)
            for position in open_positions
        )

        return {

            "allowed": total_heat < self.max_heat,

            "current_heat": round(total_heat, 2),

            "remaining_heat": round(
                max(0, self.max_heat - total_heat),
                2,
            ),
        }