class SystemHealthMonitor:

    def __init__(self):

        self.components = {}

    def update(self, component, healthy):

        self.components[component] = healthy

    def health_score(self):

        if not self.components:
            return 0

        healthy = sum(1 for status in self.components.values() if status)

        return round((healthy / len(self.components)) * 100)

    def overall_status(self):

        score = self.health_score()

        if score >= 95:
            return "EXCELLENT"

        if score >= 80:
            return "GOOD"

        if score >= 60:
            return "WARNING"

        return "CRITICAL"

    def print(self):

        print()
        print("=" * 60)
        print("SYSTEM HEALTH")
        print("=" * 60)
        print()

        for name, status in self.components.items():

            print(f"{name:20}", "OK" if status else "FAILED")

        print()
        print("Health Score :", self.health_score())
        print("Status       :", self.overall_status())