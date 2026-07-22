class DailyLossGuard:
    """
    Stops trading after the maximum daily loss is reached.
    """

    def __init__(self):

        self.max_daily_loss = 3.0  # percent

    def evaluate(self, portfolio):

        daily_loss = portfolio.get("daily_loss_percent", 0)

        if daily_loss >= self.max_daily_loss:

            return {

                "allowed": False,

                "reason": "Daily loss limit reached"

            }

        return {

            "allowed": True,

            "reason": ""

        }