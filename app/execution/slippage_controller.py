class SlippageController:

    def calculate(

        self,

        requested_price,

        executed_price

    ):

        slippage = executed_price - requested_price

        return {

            "requested": requested_price,

            "executed": executed_price,

            "slippage": round(slippage, 2)

        }

    def acceptable(

        self,

        report,

        max_slippage

    ):

        return abs(

            report["slippage"]

        ) <= max_slippage

    def print(self, report):

        print()

        print("=" * 60)

        print("SLIPPAGE REPORT")

        print("=" * 60)

        print()

        print("Requested :", report["requested"])

        print("Executed  :", report["executed"])

        print("Slippage  :", report["slippage"])