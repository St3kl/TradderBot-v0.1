class BrokerReconciliation:

    def reconcile(

        self,

        internal,

        broker

    ):

        differences = {}

        keys = set(

            internal.keys()

        ) | set(

            broker.keys()

        )

        for key in keys:

            if internal.get(key) != broker.get(key):

                differences[key] = {

                    "internal": internal.get(key),

                    "broker": broker.get(key)

                }

                internal[key] = broker.get(key)

        return {

            "updated": internal,

            "differences": differences

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("BROKER RECONCILIATION")

        print("=" * 60)

        print()

        if not report["differences"]:

            print("No differences detected.")

            return

        for key, value in report["differences"].items():

            print(

                f"{key:<15}"

                f"{value['internal']}"

                f" -> "

                f"{value['broker']}"

            )