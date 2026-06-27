from app.decision.reasons import build_reasons

indicators = {
    "rsi": 58
}

volume = {
    "strength": "Strong"
}

reasons = build_reasons(
    indicators,
    bullish=True,
    volume=volume,
    alignment=4,
    pattern="Bullish Engulfing"
)

for reason in reasons:

    print(reason)