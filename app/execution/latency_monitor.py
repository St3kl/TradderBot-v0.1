import time


class LatencyMonitor:

    def measure(self, function, *args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        latency_ms = round((end - start) * 1000, 3)

        return {

            "latency_ms": latency_ms,

            "result": result

        }

    def classify(self, latency_ms):

        if latency_ms < 50:
            return "EXCELLENT"

        if latency_ms < 150:
            return "GOOD"

        if latency_ms < 300:
            return "FAIR"

        return "POOR"

    def print(self, report):

        print()

        print("=" * 60)
        print("LATENCY MONITOR")
        print("=" * 60)
        print()

        print("Latency :", report["latency_ms"], "ms")
        print("Quality :", self.classify(report["latency_ms"]))