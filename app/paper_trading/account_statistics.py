class AccountStatistics:

    def calculate(

        self,

        starting_balance,

        current_balance,

        current_equity,

        floating_pnl

    ):

        net_profit = current_balance - starting_balance

        return_percent = (

            net_profit / starting_balance

        ) * 100

        return {

            "starting_balance": round(starting_balance, 2),

            "balance": round(current_balance, 2),

            "equity": round(current_equity, 2),

            "floating_pnl": round(floating_pnl, 2),

            "net_profit": round(net_profit, 2),

            "return_percent": round(return_percent, 2)

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("ACCOUNT STATISTICS")

        print("=" * 60)

        print()

        print("Starting Balance :", report["starting_balance"])

        print("Balance          :", report["balance"])

        print("Equity           :", report["equity"])

        print("Floating PnL     :", report["floating_pnl"])

        print("Net Profit       :", report["net_profit"])

        print("Return %         :", report["return_percent"])