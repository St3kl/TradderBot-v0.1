class AdaptivePositionSizing:

    def calculate(

        self,

        balance,

        risk_mode

    ):

        mode = risk_mode["mode"]

        if mode == "AGGRESSIVE":

            risk_percent = 2.0

        elif mode == "NORMAL":

            risk_percent = 1.0

        elif mode == "DEFENSIVE":

            risk_percent = 0.5

        else:

            risk_percent = 0.25

        risk_amount = balance * risk_percent / 100

        return {

            "mode": mode,

            "risk_percent": risk_percent,

            "risk_amount": round(risk_amount, 2)

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("ADAPTIVE POSITION SIZING")

        print("=" * 60)

        print()

        print("Mode         :", report["mode"])

        print("Risk Percent :", report["risk_percent"], "%")

        print("Risk Amount  : $", report["risk_amount"])