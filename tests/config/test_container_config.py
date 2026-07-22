from app.container.application_container import (
    ApplicationContainer
)

print()
print("=" * 40)
print("CONTAINER CONFIG")
print("=" * 40)

container = ApplicationContainer()

print(

    container.settings().get(
        "portfolio",
        "initial_balance"
    )

)

print()

print("✓ TEST PASSED")