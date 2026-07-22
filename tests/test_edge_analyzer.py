from app.analytics.edge_analyzer import EdgeAnalyzer

trades = [

    {

        "result": "WIN",

        "signals": [

            "Order Block",

            "Liquidity Sweep",

            "FVG"

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

            "Volume"

        ]

    }

]

engine = EdgeAnalyzer()

result = engine.analyze(trades)

engine.print(result)