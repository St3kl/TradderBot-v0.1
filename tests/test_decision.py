from app.decision.engine import (
    make_decision
)

confluence = {

    "score": 92,

    "strength": "Very Strong",

    "signals": [

        "EMA Trend",

        "Bullish BOS",

        "Bullish FVG"

    ],

    "missing": [

        "Liquidity Sweep"

    ]

}

decision = make_decision(
    confluence
)

print(decision)