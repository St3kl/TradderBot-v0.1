class ConfidenceStage:

    def process(self, confidence):

        return {

            "acceptable": confidence >= 70,

            "confidence": confidence

        }