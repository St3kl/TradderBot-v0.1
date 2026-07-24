from app.safety.system_health_monitor import SystemHealthMonitor

monitor = SystemHealthMonitor()

monitor.update("Broker", True)
monitor.update("MarketData", True)
monitor.update("RiskEngine", True)
monitor.update("OMS", True)
monitor.update("EMS", True)
monitor.update("Watchdog", True)
monitor.update("Recovery", False)

monitor.print()