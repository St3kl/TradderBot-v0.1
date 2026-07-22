class TrendEngine:
    """
    Determines the current market trend.

    This engine is responsible for classifying the market as:

    - Bullish
    - Bearish
    - Sideways

    using EMAs, HH/HL structure, slope, momentum, etc.
    """

    def analyze(self, session):

        trend = session.trend

        bullish = trend.get("bullish", False)

        confidence = trend.get("confidence", 0)

        direction = trend.get("direction", "Unknown")

        return {

            "direction": direction,

            "bullish": bullish,

            "confidence": confidence

        }