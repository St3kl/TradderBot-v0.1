from app.analytics.blueprint_similarity import BlueprintSimilarity

blueprint = {

    "ideal_strategy": "TREND",

    "ideal_market": "TRENDING",

    "ideal_signals": [

        "Order Block",

        "FVG",

        "Liquidity Sweep"

    ]

}

trade = {

    "strategy": "TREND",

    "market_regime": "TRENDING",

    "signals": [

        "Order Block",

        "Volume"

    ]

}

engine = BlueprintSimilarity()

result = engine.compare(

    blueprint,

    trade

)

engine.print(result)