from app.confluence.weights import WEIGHTS


def calculate_pattern_score(pattern):
    """
    Scores candlestick/chart patterns.
    """

    score = 0

    signals = []

    missing = []

    # ---------------------------------
    # Pattern Detected
    # ---------------------------------

    if pattern and pattern != "No Pattern":

        score += WEIGHTS["pattern"]

        signals.append(pattern)

    else:

        missing.append("Pattern")

    return {

        "score": score,

        "signals": signals,

        "missing": missing

    }