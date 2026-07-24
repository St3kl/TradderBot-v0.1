from datetime import datetime, UTC


class WatchdogService:

    def __init__(self):

        self.services = {}

    def heartbeat(self, service_name):

        self.services[service_name] = datetime.now(UTC)

    def is_alive(self, service_name, timeout_seconds=30):

        if service_name not in self.services:
            return False

        elapsed = (
            datetime.now(UTC) -
            self.services[service_name]
        ).total_seconds()

        return elapsed <= timeout_seconds

    def get_services(self):

        return self.services

    def print(self):

        print()

        print("=" * 60)
        print("WATCHDOG")
        print("=" * 60)
        print()

        for name in sorted(self.services):

            print(

                f"{name:20}",

                "ALIVE" if self.is_alive(name) else "TIMEOUT"

            )