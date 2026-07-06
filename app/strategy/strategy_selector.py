class StrategySelector:

    """
    Chooses the best strategy according
    to the detected market regime.
    """

    def select(self, regime):

        market = regime["regime"]

        if market == "TRENDING":
            return "TREND"

        if market == "RANGING":
            return "RANGE"

        return "DEFAULT"