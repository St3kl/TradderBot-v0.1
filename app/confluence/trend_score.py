from app.confluence.weights import WEIGHTS


def calculate_trend_score(
    bullish,
    structure
):
    """
    Scores the overall market trend.
    """

    score = 0

    signals = []

    missing = []

    # ---------------------------------
    # EMA Trend
    # ---------------------------------

    if bullish:

        score += WEIGHTS["ema_trend"]

        signals.append("EMA Trend")

    else:

        missing.append("EMA Trend")

    # ---------------------------------
    # Market Structure
    # ---------------------------------

    if structure.trend == "Bullish":

        score += WEIGHTS["market_structure"]

        signals.append("Bullish Structure")

    else:

        missing.append("Bullish Structure")

    # ---------------------------------
    # Break Of Structure
    # ---------------------------------

    if structure.bullish_bos:

        score += WEIGHTS["bos"]

        signals.append("Bullish BOS")

    else:

        missing.append("Bullish BOS")

    return {

        "score": score,

        "signals": signals,

        "missing": missing

    }