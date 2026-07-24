from app.paper_trading.position_manager import PositionManager

manager = PositionManager()

manager.add({

    "broker_order_id":"PAPER-1",

    "status":"OPEN"

})

manager.add({

    "broker_order_id":"PAPER-2",

    "status":"OPEN"

})

manager.add({

    "broker_order_id":"PAPER-3",

    "status":"CLOSED"

})

manager.print()

print()

print(manager.get("PAPER-2"))

print()

print("Open")

print(manager.open_positions())

print()

print("Closed")

print(manager.closed_positions())