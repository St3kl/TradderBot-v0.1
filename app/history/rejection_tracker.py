from collections import Counter


class RejectionTracker:

    def __init__(self):
        self.counter = Counter()

    def add(self, reasons):

        if not reasons:
            return

        for reason in reasons:
            self.counter[reason] += 1

    def statistics(self):

        total = sum(self.counter.values())

        report = {}

        for reason, count in self.counter.items():

            report[reason] = {
                "count": count,
                "percent": round(count * 100 / total, 2)
            }

        return report