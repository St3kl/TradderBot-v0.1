from app.paper_trading.realized_pnl import RealizedPnLEngine

engine = RealizedPnLEngine()

position = {

    "broker_order_id": "PAPER-000001",

    "entry": 65000,

    "quantity": 0.02,

    "direction": "LONG"

}

report = engine.calculate(

    position,

    exit_price=65300

)

engine.print(report)

print()

position["direction"] = "SHORT"

report = engine.calculate(

    position,

    exit_price=64850

)

engine.print(report)