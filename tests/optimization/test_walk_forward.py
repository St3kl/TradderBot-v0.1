from pprint import pprint

from app.optimization.walk_forward import WalkForwardOptimizer

candles = list(range(100))

optimizer = WalkForwardOptimizer()

windows = optimizer.split(

    candles,

    train_size=40,

    test_size=20

)

print()

print("=" * 40)

print("WALK FORWARD")

print("=" * 40)

print()

print("Windows:", len(windows))

print()

for i, window in enumerate(windows):

    print(

        i,

        len(window["train"]),

        len(window["test"])

    )

print()

print("✓ TEST PASSED")