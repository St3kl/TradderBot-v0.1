from app.adaptive.strategy_optimizer import StrategyOptimizer

learning = {

    "TREND": {

        "win_rate": 78,

        "total": 65

    },

    "RANGE": {

        "win_rate": 34,

        "total": 40

    },

    "BREAKOUT": {

        "win_rate": 52,

        "total": 23

    },

    "SCALPING": {

        "win_rate": 0,

        "total": 4

    }

}

engine = StrategyOptimizer()

result = engine.optimize(learning)

engine.print(result)