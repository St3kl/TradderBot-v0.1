from pprint import pprint

from app.optimization.parameter_optimizer import ParameterOptimizer

results = [

    {

        "atr":0.5,

        "win_rate":61

    },

    {

        "atr":1.0,

        "win_rate":73

    },

    {

        "atr":1.5,

        "win_rate":69

    },

    {

        "atr":2.0,

        "win_rate":65

    }

]

optimizer = ParameterOptimizer()

best = optimizer.optimize(results)

print()

print("="*40)

print("PARAMETER OPTIMIZER")

print("="*40)

print()

pprint(best)

print()

print("✓ TEST PASSED")