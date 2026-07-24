class PaperTradingDashboard:

    def render(

        self,

        account,

        performance,

        current_signal,

        positions

    ):

        print()

        print("=" * 70)

        print("TRADDERBOT LIVE PAPER TRADING DASHBOARD")

        print("=" * 70)

        print()

        print("ACCOUNT")

        print("------------------------------")

        print("Balance :", account["balance"])

        print("Equity  :", account["equity"])

        print("PnL     :", account["floating_pnl"])

        print()

        print("PERFORMANCE")

        print("------------------------------")

        print("Trades     :", performance["total_trades"])

        print("Win Rate   :", performance["win_rate"], "%")

        print("Profit     :", performance["total_profit"])

        print()

        print("CURRENT SIGNAL")

        print("------------------------------")

        print("Symbol     :", current_signal["symbol"])

        print("Direction  :", current_signal["signal"])

        print("Confidence :", current_signal["confidence"])

        print()

        print("OPEN POSITIONS")

        print("------------------------------")

        if not positions:

            print("None")

        else:

            for p in positions:

                print(

                    p["symbol"],

                    p["direction"],

                    p["entry"]

                )

        print()

        print("=" * 70)