from app.analytics.trade_attribution import TradeAttribution

trades = [

    {

        "signals": [

            "Order Block",

            "FVG",

            "Liquidity Sweep",

        ],

        "result": "WIN",

    },

    {

        "signals": [

            "Order Block",

            "Volume",

        ],

        "result": "LOSS",

    },

    {

        "signals": [

            "Order Block",

            "FVG",

        ],

        "result": "WIN",

    },

]

engine = TradeAttribution()

print(engine.analyze(trades))