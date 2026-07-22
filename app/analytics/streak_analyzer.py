class StreakAnalyzer:

    def analyze(self, trades):

        longest_win = 0
        longest_loss = 0

        current_win = 0
        current_loss = 0

        for trade in trades:

            if trade["result"] == "WIN":

                current_win += 1
                current_loss = 0

            else:

                current_loss += 1
                current_win = 0

            longest_win = max(

                longest_win,

                current_win

            )

            longest_loss = max(

                longest_loss,

                current_loss

            )

        return {

            "longest_win_streak": longest_win,

            "longest_loss_streak": longest_loss

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("STREAK ANALYSIS")

        print("=" * 60)

        print()

        print(

            "Longest Win Streak :",

            report["longest_win_streak"]

        )

        print(

            "Longest Loss Streak:",

            report["longest_loss_streak"]

        )