def calculate_confluence(
    bullish,
    pattern,
    structure,
    volume,
    alignment,
    smart_money
):
    """
    Build a complete confluence score.
    """

    score = 0
    signals = []
    missing = []

    # -----------------------
    # EMA Trend
    # -----------------------

    if bullish:
        score += 10
        signals.append("EMA Trend")
    else:
        missing.append("EMA Trend")

    # -----------------------
    # Market Structure
    # -----------------------

    if structure["trend"] == "Bullish":
        score += 15
        signals.append("Bullish Structure")
    else:
        missing.append("Bullish Structure")

    # -----------------------
    # Break of Structure
    # -----------------------

    if structure["bos"]["type"] == "Bullish BOS":
        score += 15
        signals.append("Bullish BOS")
    else:
        missing.append("Bullish BOS")

    # -----------------------
    # Volume
    # -----------------------

    if volume["score"] >= 15:
        score += 10
        signals.append("Strong Volume")
    else:
        missing.append("Strong Volume")

    # -----------------------
    # Pattern
    # -----------------------

    if pattern != "No Pattern":
        score += 10
        signals.append(pattern)
    else:
        missing.append("Pattern")

    # -----------------------
    # Multi-Timeframe
    # -----------------------

    if alignment >= 3:
        score += 10
        signals.append("MTF Alignment")
    else:
        missing.append("MTF Alignment")

    # -----------------------
    # Bullish Order Blocks
    # -----------------------

    if smart_money["order_blocks"]["bullish"] > 0:
        score += 10
        signals.append("Bullish Order Block")
    else:
        missing.append("Bullish Order Block")

    # -----------------------
    # Bullish Fair Value Gaps
    # -----------------------

    if smart_money["fair_value_gaps"]["bullish"] > 0:
        score += 10
        signals.append("Bullish FVG")
    else:
        missing.append("Bullish FVG")

    # -----------------------
    # Discount Zone
    # -----------------------

    if smart_money["premium_discount"]["zone"] == "Discount":
        score += 10
        signals.append("Discount Zone")
    else:
        missing.append("Discount Zone")

    # -----------------------
    # Strength
    # -----------------------

    if score >= 90:
        strength = "Very Strong"
    elif score >= 75:
        strength = "Strong"
    elif score >= 60:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "score": score,
        "strength": strength,
        "signals": signals,
        "missing": missing
    }