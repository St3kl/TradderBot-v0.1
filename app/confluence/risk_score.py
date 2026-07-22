from app.confluence.weights import WEIGHTS


def calculate_risk_score(
    validation
):
    """
    Scores trade validation.
    """

    score = 0

    signals = []

    missing = []

    if validation["valid"]:

        score += WEIGHTS["risk_validation"]

        signals.append("Trade Validated")

    else:

        missing.append("Trade Validation")

    return {

        "score": score,

        "signals": signals,

        "missing": missing

    }