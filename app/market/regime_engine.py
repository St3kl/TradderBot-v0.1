class RegimeEngine:

    """
    Determines the current market regime.
    """

    def classify(self, indicators):

        adx = indicators["adx"]
        atr = indicators["atr"]

        if adx >= 30:

            regime = "TRENDING"

        elif adx <= 20:

            regime = "RANGING"

        else:

            regime = "TRANSITION"

        if atr >= 1000:

            volatility = "HIGH"

        else:

            volatility = "NORMAL"

        return {

            "regime": regime,

            "volatility": volatility

        }