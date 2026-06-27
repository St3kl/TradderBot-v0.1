def calculate_confluence(
    bullish,
    pattern,
    structure,
    volume,
    alignment
):
    """
    Calculate market confluence.
    """

    signals = []

    if bullish:
        signals.append("EMA Trend")

    if pattern != "No Pattern":
        signals.append("Pattern")

    if structure["bos"]["type"] == "Bullish BOS":
        signals.append("Bullish BOS")

    if structure["trend"] == "Bullish":
        signals.append("Bullish Structure")

    if volume["score"] >= 15:
        signals.append("Strong Volume")

    if alignment >= 3:
        signals.append("MTF Alignment")

    return {
        "count": len(signals),
        "signals": signals
    }