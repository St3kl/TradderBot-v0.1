from app.paper_trading.unrealized_pnl import UnrealizedPnLEngine

engine = UnrealizedPnLEngine()

position = {

    "broker_order_id":"PAPER-000001",

    "entry":65000,

    "quantity":0.02,

    "direction":"LONG"

}

report = engine.calculate(

    position,

    current_price=65250

)

engine.print(report)

print()

position["direction"] = "SHORT"

report = engine.calculate(

    position,

    current_price=64800

)

engine.print(report)