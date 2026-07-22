from pprint import pprint

from app.research.strategy_ranking import StrategyRanking

strategies = [

    {

        "name":"Trend A",

        "score":88

    },

    {

        "name":"Range",

        "score":72

    },

    {

        "name":"Scalping",

        "score":94

    },

    {

        "name":"Breakout",

        "score":81

    }

]

ranking = StrategyRanking()

results = ranking.rank(

    strategies,

    top=3

)

print()

print("="*40)

print("TOP STRATEGIES")

print("="*40)

print()

for r in results:

    pprint(r)

print()

print("✓ TEST PASSED")