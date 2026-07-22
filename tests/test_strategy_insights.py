from app.ai.strategy_insights import StrategyInsights

stats = {

    "TREND": {

        "win_rate": 76,

        "total": 52

    },

    "RANGE": {

        "win_rate": 58,

        "total": 31

    },

    "BREAKOUT": {

        "win_rate": 43,

        "total": 28

    },

    "SCALPING": {

        "win_rate": 21,

        "total": 19

    },

    "REVERSAL": {

        "win_rate": 0,

        "total": 5

    }

}

engine = StrategyInsights()

result = engine.analyze(stats)

engine.print(result)