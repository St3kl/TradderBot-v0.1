from pprint import pprint

from app.learning.strategy_ranking import StrategyRanking

statistics = {

    "TREND": {

        "win_rate": 72,

        "total": 84

    },

    "RANGE": {

        "win_rate": 55,

        "total": 120

    },

    "BREAKOUT": {

        "win_rate": 81,

        "total": 40

    }

}

ranking = StrategyRanking().rank(

    statistics

)

pprint(ranking)