import csv
import os


class TradeJournal:

    def __init__(self, filename="logs/trade_journal.csv"):

        self.filename = filename

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        if not os.path.exists(filename):

            with open(filename, "w", newline="") as f:

                writer = csv.writer(f)

                writer.writerow([
                    "time",
                    "symbol",
                    "strategy",
                    "direction",
                    "entry",
                    "exit",
                    "stop",
                    "take_profit",
                    "rr",
                    "position_size",
                    "profit",
                    "result",
                    "confidence"
                ])

    def save(self, trade):

        with open(self.filename, "a", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                trade.get("time"),
                trade.get("symbol"),
                trade.get("strategy"),
                trade.get("direction"),
                trade.get("entry"),
                trade.get("exit"),
                trade.get("stop_loss"),
                trade.get("take_profit"),
                trade.get("risk_reward"),
                trade.get("position_size"),
                trade.get("profit"),
                trade.get("result"),
                trade.get("confidence")
            ])