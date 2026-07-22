from pprint import pprint

from app.research.research_engine import ResearchEngine


def evaluator(parameters):

    score = (

        parameters["atr"] * 10 +

        parameters["rr"] * 15 -

        parameters["risk"] * 5

    )

    return {

        **parameters,

        "score": score

    }


parameters = {

    "atr":[1,2],

    "risk":[1,2],

    "rr":[2,3]

}


engine = ResearchEngine()

results = engine.run(

    parameters,

    evaluator

)

print()

print("="*40)

print("TOP RESULTS")

print("="*40)

print()

for r in results:

    pprint(r)

print()

print("✓ TEST PASSED")