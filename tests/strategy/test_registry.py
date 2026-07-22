from app.strategy.registry import StrategyRegistry


class Dummy:

    name = "ABC"


def main():

    registry = StrategyRegistry()

    registry.register(Dummy())

    assert registry.get("ABC") is not None

    assert len(registry.all()) == 1

    print()
    print("=" * 40)
    print("REGISTRY TEST PASSED")
    print("=" * 40)


if __name__ == "__main__":

    main()