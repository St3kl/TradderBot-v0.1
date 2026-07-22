class RejectionAnalyzer:

    def analyze(self, checklist):

        reasons = []

        for item, passed in checklist.items():

            if not passed:

                reasons.append(item)

        return reasons