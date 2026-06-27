from app.decision.confidence import calculate_confidence

tests = [
    (95, 20, 4, True),
    (85, 15, 3, True),
    (72, 12, 2, True),
    (55, 10, 1, False),
]

for score, volume, alignment, bullish in tests:

    confidence = calculate_confidence(
        score,
        volume,
        alignment,
        bullish
    )

    print(
        score,
        "->",
        confidence,
        "%"
    )