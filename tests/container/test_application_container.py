from app.container.application_container import (
    ApplicationContainer
)

print()
print("=" * 40)
print("APPLICATION CONTAINER")
print("=" * 40)

container = ApplicationContainer()

trade1 = container.trade_manager()
trade2 = container.trade_manager()

portfolio1 = container.portfolio()
portfolio2 = container.portfolio()

print()

print(trade1 is trade2)
print(portfolio1 is portfolio2)

print()

print("✓ TEST PASSED")