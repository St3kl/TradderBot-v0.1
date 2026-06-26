def calculate_score(
    indicators,
    bullish,
    volume_score,
    alignment,
    pattern
):
    """
    Returns a score from 0 to 100.
    """

    score = 0

    breakdown = {}

    # -----------------------------
    # Trend (25 pts)
    # -----------------------------
    if bullish:
        score += 25
        breakdown["Trend"] = 25
    else:
        breakdown["Trend"] = 0

    # -----------------------------
    # RSI (20 pts)
    # -----------------------------
    rsi = indicators["rsi"]

    if 55 <= rsi <= 65:
        rsi_score = 20

    elif 50 <= rsi < 55:
        rsi_score = 15

    elif 45 <= rsi < 50:
        rsi_score = 10

    else:
        rsi_score = 5

    score += rsi_score
    breakdown["RSI"] = rsi_score

    # -----------------------------
    # Volume (20 pts)
    # -----------------------------
    volume_score = min(volume_score, 20)

    score += volume_score
    breakdown["Volume"] = volume_score

    # -----------------------------
    # Multi Timeframe (25 pts)
    # -----------------------------
    mtf_score = round(
        alignment * 25 / 4
    )

    score += mtf_score

    breakdown["MTF"] = mtf_score

    # -----------------------------
    # Pattern (10 pts)
    # -----------------------------
    if pattern != "No Pattern":

        score += 10

        breakdown["Pattern"] = 10

    else:

        breakdown["Pattern"] = 0

    return {
        "score": round(score),
        "breakdown": breakdown
    }


def get_grade(score):

    if score >= 95:
        return "A+ Elite"

    elif score >= 90:
        return "A+"

    elif score >= 85:
        return "A"

    elif score >= 75:
        return "B"

    elif score >= 65:
        return "C"

    else:
        return "Avoid"