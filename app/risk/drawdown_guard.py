class DrawdownGuard:
    """
    Stops trading after excessive account drawdown.
    """

    def __init__(self):

        self.max_drawdown = 10.0  # percent

    def evaluate(self, portfolio):

        dd = portfolio.get("max_drawdown", 0)

        if dd >= self.max_drawdown:

            return {

                "allowed": False,

                "reason": "Maximum drawdown exceeded"

            }

        return {

            "allowed": True,

            "reason": ""

        }