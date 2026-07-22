from pprint import pprint

from app.learning.context_strategy_advisor import ContextStrategyAdvisor

market = {

    "TRENDING | NORMAL": {

        "best_strategy": "TREND",

        "win_rate": 82

    },

    "RANGING | NORMAL": {

        "best_strategy": "RANGE",

        "win_rate": 71

    }

}

advisor = ContextStrategyAdvisor()

pprint(

    advisor.recommend(

        market,

        "TRENDING",

        "NORMAL"

    )

)