from app.strategy.strategy_engine import StrategyEngine
from app.strategy.base_strategy import BaseStrategy


class DummySession:

    def __init__(self):

        self.strategy = "TEST"

        self.executed = False


class TestStrategy(BaseStrategy):

    name = "TEST"

    def evaluate(self, session):

        session.executed = True

        return session


def main():

    engine = StrategyEngine()

    engine.register(TestStrategy())

    session = DummySession()

    engine.evaluate(session)

    assert session.executed is True

    print()
    print("=" * 40)
    print("STRATEGY ENGINE TEST PASSED")
    print("=" * 40)


if __name__ == "__main__":

    main()