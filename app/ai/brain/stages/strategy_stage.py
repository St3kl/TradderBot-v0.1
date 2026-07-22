class StrategyStage:

    def process(self, strategy):

        if strategy:

            return {

                "valid": True,

                "strategy": strategy

            }

        return {

            "valid": False,

            "strategy": None

        }