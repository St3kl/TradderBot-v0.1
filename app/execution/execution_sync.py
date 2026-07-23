class ExecutionSync:

    def sync(

        self,

        order,

        broker_update

    ):

        changes = {}

        for key, value in broker_update.items():

            if order.get(key) != value:

                changes[key] = {

                    "old": order.get(key),

                    "new": value

                }

                order[key] = value

        return {

            "order": order,

            "changes": changes

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("EXECUTION SYNCHRONIZATION")

        print("=" * 60)

        print()

        if not report["changes"]:

            print("Already synchronized.")

            return

        for key, value in report["changes"].items():

            print(

                f"{key:<12}"

                f"{value['old']}"

                f" -> "

                f"{value['new']}"

            )