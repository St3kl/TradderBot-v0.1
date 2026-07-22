from app.analytics.best_trade_profile import BestTradeProfile

trades = [

    {

        "result": "WIN",

        "signals": [

            "Order Block",

            "FVG"

        ],

        "strategy": "TREND",

        "market_regime": "TRENDING"

    },

    {

        "result": "WIN",

        "signals": [

            "Order Block",

            "Liquidity Sweep"

        ],

        "strategy": "TREND",

        "market_regime": "TRENDING"

    },

    {

        "result": "WIN",

        "signals": [

            "FVG"

        ],

        "strategy": "BREAKOUT",

        "market_regime": "VOLATILE"

    },

    {

        "result": "LOSS",

        "signals": [

            "Volume"

        ],

        "strategy": "RANGE",

        "market_regime": "RANGING"

    }

]

engine = BestTradeProfile()

result = engine.analyze(trades)

engine.print(result)