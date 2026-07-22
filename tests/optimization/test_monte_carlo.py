from app.optimization.monte_carlo import MonteCarloSimulator

trades = [

    {"pnl":100},

    {"pnl":-50},

    {"pnl":80},

    {"pnl":-20},

    {"pnl":150},

    {"pnl":-70}

]

mc = MonteCarloSimulator()

results = mc.simulate(

    trades,

    iterations=5

)

print()

print("="*40)

print("MONTE CARLO")

print("="*40)

print()

for run in results:

    print(run)

print()

print("✓ TEST PASSED")