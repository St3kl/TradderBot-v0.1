from app.safety.auto_recovery_manager import AutoRecoveryManager

manager = AutoRecoveryManager()

print()

print("Broker Recovery:",
      manager.recover("Broker"))

print("MarketData Recovery:",
      manager.recover("MarketData"))

print("Analyzer Recovery:",
      manager.recover("Analyzer"))

manager.print()