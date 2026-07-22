class BacktestComparator:

    def compare(self, old_report, new_report):

        old_balance = old_report["portfolio"]["balance"]
        new_balance = new_report["portfolio"]["balance"]

        old_wr = old_report["performance"]["winrate"]
        new_wr = new_report["performance"]["winrate"]

        return {

            "balance_change": round(new_balance - old_balance, 2),

            "winrate_change": round(new_wr - old_wr, 2),

            "improved_balance": new_balance > old_balance,

            "improved_winrate": new_wr > old_wr

        }

    def print(self, comparison):

        print()

        print("=" * 60)
        print("BACKTEST COMPARISON")
        print("=" * 60)

        print(f"Balance Change : {comparison['balance_change']}")
        print(f"Winrate Change : {comparison['winrate_change']}%")

        print(f"Balance Improved : {comparison['improved_balance']}")
        print(f"Winrate Improved : {comparison['improved_winrate']}")