class EquityEngine:

    def calculate(

        self,

        balance,

        unrealized_positions

    ):

        floating = sum(

            p["unrealized_pnl"]

            for p in unrealized_positions

        )

        equity = balance + floating

        return {

            "balance": round(balance, 2),

            "floating_pnl": round(floating, 2),

            "equity": round(equity, 2)

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("ACCOUNT EQUITY")

        print("=" * 60)

        print()

        print("Balance      :", report["balance"])

        print("FloatingPnL  :", report["floating_pnl"])

        print("Equity       :", report["equity"])