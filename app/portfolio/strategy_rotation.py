class StrategyRotation:

    def rotate(self, strategies):

        ranked = sorted(

            strategies,

            key=lambda s: s["score"],

            reverse=True

        )

        active = []

        standby = []

        disabled = []

        for strategy in ranked:

            if strategy["score"] >= 80:

                active.append(strategy["name"])

            elif strategy["score"] >= 60:

                standby.append(strategy["name"])

            else:

                disabled.append(strategy["name"])

        return {

            "active": active,

            "standby": standby,

            "disabled": disabled,

            "ranking": ranked

        }

    def print(self, report):

        print()

        print("=" * 60)
        print("STRATEGY ROTATION")
        print("=" * 60)

        print()

        print("ACTIVE")

        for s in report["active"]:
            print("-", s)

        print()

        print("STANDBY")

        for s in report["standby"]:
            print("-", s)

        print()

        print("DISABLED")

        for s in report["disabled"]:
            print("-", s)