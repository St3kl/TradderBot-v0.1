from app.analytics.signal_combination_analyzer import SignalCombinationAnalyzer

trades = [

    {

        "result": "WIN",

        "signals": [

            "Order Block",

            "FVG",

            "Liquidity Sweep"

        ]

    },

    {

        "result": "WIN",

        "signals": [

            "Order Block",

            "FVG"

        ]

    },

    {

        "result": "LOSS",

        "signals": [

            "Order Block",

            "Volume"

        ]

    },

    {

        "result": "LOSS",

        "signals": [

            "Volume",

            "Liquidity Sweep"

        ]

    }

]

engine = SignalCombinationAnalyzer()

result = engine.analyze(trades)

engine.print(result)