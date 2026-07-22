class StrategyRegistry:

    def __init__(self):

        self._strategies = {}

    # -----------------------------

    def register(self, strategy):

        self._strategies[strategy.name] = strategy

    # -----------------------------

    def get(self, name):

        return self._strategies.get(name)

    # -----------------------------

    def all(self):

        return self._strategies