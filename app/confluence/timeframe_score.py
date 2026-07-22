from app.confluence.weights import WEIGHTS


def calculate_timeframe_score(
    alignment
):
    """
    Scores multi-timeframe agreement.
    """

    score = 0

    signals = []

    missing = []

    if alignment >= 3:

        score += WEIGHTS["mtf"]

        signals.append("Multi-Timeframe Alignment")

    else:

        missing.append("Multi-Timeframe Alignment")

    return {

        "score": score,

        "signals": signals,

        "missing": missing

    }