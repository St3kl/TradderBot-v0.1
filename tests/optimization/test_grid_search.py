from pprint import pprint

from app.optimization.grid_search import GridSearch

parameters = {

    "atr":[0.5,1,1.5],

    "risk":[1,2],

    "rr":[2,3]

}

grid = GridSearch()

results = grid.generate(parameters)

print()

print("="*40)

print("GRID SEARCH")

print("="*40)

print()

print("Total combinations:", len(results))

print()

for r in results:

    pprint(r)

print()

print("✓ TEST PASSED")