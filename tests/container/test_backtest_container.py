from app.container.application_container import (
    ApplicationContainer
)

print()
print("=" * 40)
print("BACKTEST CONTAINER")
print("=" * 40)

container = ApplicationContainer()

backtest = container.backtest()

print(type(backtest.execution).__name__)
print(type(backtest.learning).__name__)
print(type(backtest.trade_manager).__name__)
print(type(backtest.portfolio).__name__)
print(type(backtest.paper).__name__)

print()
print("✓ TEST PASSED")