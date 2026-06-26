def detect_bos(
    closes,
    swing_highs,
    swing_lows
):
    """
    Detect Break of Structure (BOS).

    Returns:

    Bullish BOS
    Bearish BOS
    No BOS
    """

    latest_close = closes[-1]

    # -----------------------------
    # Bullish BOS
    # -----------------------------

    if swing_highs:

        last_high = swing_highs[-1][1]

        if latest_close > last_high:

            return {
                "type": "Bullish BOS",
                "level": last_high
            }

    # -----------------------------
    # Bearish BOS
    # -----------------------------

    if swing_lows:

        last_low = swing_lows[-1][1]

        if latest_close < last_low:

            return {
                "type": "Bearish BOS",
                "level": last_low
            }

    return {
        "type": "No BOS",
        "level": None
    }