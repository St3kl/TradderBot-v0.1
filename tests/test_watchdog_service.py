import time

from app.safety.watchdog_service import WatchdogService

watchdog = WatchdogService()

watchdog.heartbeat("Analyzer")
watchdog.heartbeat("OMS")
watchdog.heartbeat("Broker")

watchdog.print()

print()

time.sleep(2)

print("Analyzer Alive:", watchdog.is_alive("Analyzer", 5))

print("Analyzer Alive (1 sec timeout):",
      watchdog.is_alive("Analyzer", 1))