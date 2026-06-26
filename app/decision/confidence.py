def calculate_confidence(
    score,
    volume_score,
    alignment,
    bullish
):
    """
    Calculates a confidence percentage (0–100)
    based on the quality of the setup.
    """

    confidence = 0

    # -------------------------
    # Score (0–50)
    # -------------------------
    confidence += score * 0.5

    # -------------------------
    # Volume (0–20)
    # -------------------------
    confidence += min(volume_score, 20)

    # -------------------------
    # Multi-Timeframe (0–20)
    # -------------------------
    confidence += alignment * 5

    # -------------------------
    # Trend (10)
    # -------------------------
    if bullish:
        confidence += 10

    confidence = round(confidence)

    return min(confidence, 100)