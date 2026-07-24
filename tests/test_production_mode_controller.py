from app.safety.production_mode_controller import (
    ProductionModeController,
    TradingMode
)

controller = ProductionModeController()

controller.print()

print()

controller.set_mode(TradingMode.PAPER)

controller.print()

print()

controller.set_mode(TradingMode.STAGING)

controller.print()

print()

controller.set_mode(TradingMode.LIVE)

controller.print()