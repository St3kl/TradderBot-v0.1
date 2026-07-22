class ScoreBreakdown:

    def calculate(self, checklist):

        passed = sum(checklist.values())

        total = len(checklist)

        score = round(

            passed / total * 100,

            2

        )

        return {

            "passed": passed,

            "total": total,

            "score": score

        }