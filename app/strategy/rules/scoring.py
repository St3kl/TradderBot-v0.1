def calculate_confidence(
    indicators,
    pattern
):

    score = 50

    if indicators["ema50"] > indicators["ema200"]:
        score += 15

    if indicators["rsi"] > 55:
        score += 10

    if pattern != "Unknown":
        score += 15

    return min(score, 100)