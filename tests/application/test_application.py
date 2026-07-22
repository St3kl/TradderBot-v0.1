from app.application import Application

print()
print("=" * 40)
print("APPLICATION")
print("=" * 40)

app = Application()

print(type(app.backtest).__name__)
print(type(app.trading_engine).__name__)
print(type(app.execution).__name__)
print(type(app.learning).__name__)

print()
print("✓ TEST PASSED")