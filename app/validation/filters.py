def apply_filters(
    indicators,
    bullish,
    volume_score,
    alignment,
    atr
):
    """
    Pre-trade filters:
    Determines if a trade should even be evaluated.
    """

    reasons = []

    # -----------------------
    # Trend filter
    # -----------------------
    if indicators["ema50"] == indicators["ema200"]:
        return False, ["No clear trend"]

    # -----------------------
    # Volume filter
    # -----------------------
    if volume_score < 10:
        return False, ["Weak volume"]

    # -----------------------
    # ATR filter (market activity)
    # -----------------------
    if atr is not None and atr < 0.0001:
        return False, ["Market too slow (low volatility)"]

    # -----------------------
    # Multi-timeframe filter
    # -----------------------
    if alignment < 2:
        reasons.append("Weak timeframe alignment")

    # -----------------------
    # Final decision
    # -----------------------
    if len(reasons) == 0:
        return True, ["All filters passed"]

    return True, reasons