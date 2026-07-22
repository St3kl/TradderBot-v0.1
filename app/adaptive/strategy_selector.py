class StrategySelector:

    def choose(self, ranking):

        if not ranking:

            return "DEFAULT"

        return ranking[0]["strategy"]