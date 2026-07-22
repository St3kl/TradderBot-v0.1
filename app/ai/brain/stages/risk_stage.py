class RiskStage:

    def process(self, risk):

        return {

            "acceptable": risk <= 2,

            "risk": risk

        }