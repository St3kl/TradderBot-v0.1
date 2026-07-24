class CircuitBreaker:

    def __init__(self, max_failures=3):

        self.max_failures = max_failures
        self.failures = 0
        self.open = False

    def record_failure(self):

        self.failures += 1

        if self.failures >= self.max_failures:
            self.open = True

    def reset(self):

        self.failures = 0
        self.open = False

    def is_open(self):

        return self.open

    def print(self):

        print()
        print("=" * 60)
        print("CIRCUIT BREAKER")
        print("=" * 60)
        print()

        print("Failures :", self.failures)
        print("Open      :", self.open)