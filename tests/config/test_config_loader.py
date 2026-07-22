from app.config.config_loader import ConfigLoader

print()
print("=" * 40)
print("CONFIG LOADER")
print("=" * 40)

config = ConfigLoader()

print("Application:", config.get("application", "name"))
print("Mode:", config.get("application", "mode"))
print("Balance:", config.get("portfolio", "initial_balance"))
print("Risk:", config.get("risk", "risk_percent"))

print()
print("✓ TEST PASSED")