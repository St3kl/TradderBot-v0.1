from app.confluence.weights import WEIGHTS


def calculate_volume_score(volume):
    """
    Scores market volume confirmation.
    """

    score = 0

    signals = []

    missing = []

    volume_score = volume.get("score", 0)

    if volume_score >= 70:

        score += WEIGHTS["volume"]

        signals.append("Strong Volume")

    else:

        missing.append("Strong Volume")

    return {

        "score": score,

        "signals": signals,

        "missing": missing

    }