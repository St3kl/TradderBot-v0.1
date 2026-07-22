from pprint import pprint

from app.learning.strategy_advisor import StrategyAdvisor

ranking = [

    {

        "strategy": "BREAKOUT",

        "win_rate": 81,

        "trades": 40

    },

    {

        "strategy": "TREND",

        "win_rate": 72,

        "trades": 85

    },

    {

        "strategy": "RANGE",

        "win_rate": 55,

        "trades": 150

    }

]

advisor = StrategyAdvisor()

pprint(

    advisor.recommend(ranking)

)