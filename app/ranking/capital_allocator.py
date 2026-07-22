class CapitalAllocator:

    """
    Allocates risk according to trade quality.
    """

    def allocate(self, ranked_trade, balance):

        score = ranked_trade["score"]

        if score >= 90:
            risk = 2.0

        elif score >= 80:
            risk = 1.5

        elif score >= 70:
            risk = 1.0

        elif score >= 60:
            risk = 0.5

        else:
            risk = 0.25

        return {
            "risk_percent": risk,
            "risk_amount": round(balance * risk / 100, 2)
        }