class StrategyScore:

    def calculate(

        self,

        winrate,

        expectancy,

        recovery,

        quality,

        stability

    ):

        score = (

            winrate * 0.20 +

            expectancy * 0.25 +

            recovery * 0.20 +

            quality * 0.20 +

            stability * 0.15

        )

        if score >= 90:

            grade = "A+"

        elif score >= 80:

            grade = "A"

        elif score >= 70:

            grade = "B"

        elif score >= 60:

            grade = "C"

        else:

            grade = "D"

        return {

            "score": round(score, 2),

            "grade": grade

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("STRATEGY SCORE")

        print("=" * 60)

        print()

        print("Overall Score :", report["score"])

        print("Grade         :", report["grade"])