import csv


class DatasetLoader:
    """
    Loads historical candles from CSV files.
    """

    def load(self, filename):

        candles = []

        with open(filename, newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                candles.append({

                    "time": row["time"],

                    "open": float(row["open"]),

                    "high": float(row["high"]),

                    "low": float(row["low"]),

                    "close": float(row["close"]),

                    "volume": float(row["volume"])

                })

        print(f"Loaded {len(candles)} candles")

        return candles