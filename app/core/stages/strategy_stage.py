from app.strategy.strategy_engine import StrategyEngine


class StrategyStage:

    def __init__(self):

        self.engine = StrategyEngine()

    def run(self, session):

        print("Running Strategy Stage")

        session = self.engine.evaluate(session)

        return session