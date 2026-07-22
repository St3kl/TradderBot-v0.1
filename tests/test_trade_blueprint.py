from app.analytics.trade_blueprint import TradeBlueprint

profile = {

    "signals": {

        "Order Block": 8,

        "FVG": 7,

        "Liquidity Sweep": 5,

        "Volume": 2

    },

    "strategies": {

        "TREND": 6,

        "BREAKOUT": 3

    },

    "market_regimes": {

        "TRENDING": 7,

        "VOLATILE": 2

    }

}

combinations = {

    "Order Block + FVG": {

        "win_rate": 91

    },

    "FVG + Liquidity Sweep": {

        "win_rate": 88

    },

    "Order Block + Liquidity Sweep": {

        "win_rate": 82

    }

}

engine = TradeBlueprint()

blueprint = engine.build(

    profile,

    combinations

)

engine.print(blueprint)