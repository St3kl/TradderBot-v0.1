def make_decision(confluence):
    """
    Converts confluence analysis
    into a trading decision.
    """

    score = confluence["score"]

    if score >= 90:

        action = "STRONG BUY"

        confidence = 95

        risk = "LOW"

    elif score >= 75:

        action = "BUY"

        confidence = 85

        risk = "MEDIUM"

    elif score >= 60:

        action = "WATCH"

        confidence = 65

        risk = "MEDIUM"

    else:

        action = "NO TRADE"

        confidence = 40

        risk = "HIGH"

    return {

        "action": action,

        "score": score,

        "strength": confluence["strength"],

        "confidence": confidence,

        "risk": risk,

        "signals": confluence["signals"],

        "missing": confluence["missing"]

    }