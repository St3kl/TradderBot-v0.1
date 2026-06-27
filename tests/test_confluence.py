from app.confluence.engine import (
    calculate_confluence
)

structure = {
    "trend": "Bullish",
    "bos": {
        "type": "Bullish BOS"
    }
}

volume = {
    "score": 20
}

result = calculate_confluence(
    bullish=True,
    pattern="Bullish Engulfing",
    structure=structure,
    volume=volume,
    alignment=4
)

print(result)