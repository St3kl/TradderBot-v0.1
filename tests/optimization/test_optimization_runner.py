from pprint import pprint

from app.optimization.grid_search import GridSearch
from app.optimization.optimization_runner import OptimizationRunner


def evaluator(parameters):

    return {

        **parameters,

        "score": sum(parameters.values())

    }


parameters = {

    "atr":[1,2],

    "risk":[1,2],

    "rr":[2,3]

}

grid = GridSearch()

sets = grid.generate(parameters)

runner = OptimizationRunner()

results = runner.run(

    sets,

    evaluator

)

print()

print("=" * 40)

print("OPTIMIZATION RUNNER")

print("=" * 40)

print()

print("Runs:", len(results))

print()

for r in results:

    pprint(r)

print()

print("✓ TEST PASSED")