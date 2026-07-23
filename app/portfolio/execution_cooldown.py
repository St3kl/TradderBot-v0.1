from datetime import datetime, timedelta


class ExecutionCooldown:

    def check(

        self,

        symbol,

        history,

        cooldown_minutes=30,

        now=None

    ):

        if now is None:

            now = datetime.utcnow()

        for trade in reversed(history):

            if trade["symbol"] != symbol:

                continue

            last_exit = trade["closed_at"]

            if now < last_exit + timedelta(minutes=cooldown_minutes):

                return {

                    "allowed": False,

                    "remaining_minutes":

                        round(

                            (

                                last_exit

                                + timedelta(minutes=cooldown_minutes)

                                - now

                            ).total_seconds()

                            / 60,

                            1

                        )

                }

            break

        return {

            "allowed": True,

            "remaining_minutes": 0

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("EXECUTION COOLDOWN")

        print("=" * 60)

        print()

        print("Allowed :", report["allowed"])

        print("Remaining Minutes :", report["remaining_minutes"])