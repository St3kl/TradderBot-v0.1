from app.decision.engine import make_decision

indicators = {

    "ema50": 100,

    "ema200": 90,

    "rsi": 58,

    "atr": 120

}

volume = {

    "strength": "Strong",

    "score": 18

}

decision = make_decision(

    indicators,

    bullish=True,

    volume=volume,

    alignment=4,

    pattern="Bullish Engulfing"

)

print()

print(decision)