from app.decision.actions import decide_action


tests = [

    (95, True),

    (90, False),

    (80, True),

    (80, False),

    (65, True),

    (45, True)

]


for score, bullish in tests:

    print(
        score,
        bullish,
        "->",
        decide_action(
            score,
            bullish
        )
    )