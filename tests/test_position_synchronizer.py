from app.execution.position_synchronizer import PositionSynchronizer

sync = PositionSynchronizer()

broker_positions = [

    {

        "symbol": "BTCUSDT",

        "direction": "LONG",

        "quantity": 0.02

    },

    {

        "symbol": "EURUSD",

        "direction": "SELL",

        "quantity": 0.50

    }

]

sync.synchronize(broker_positions)

sync.print()

print()

print(sync.get_positions())