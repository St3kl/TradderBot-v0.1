from app.execution.order_synchronizer import OrderSynchronizer

sync = OrderSynchronizer()

broker_orders = [

    {

        "broker_order_id": "BN-1001",

        "symbol": "BTCUSDT",

        "status": "FILLED"

    },

    {

        "broker_order_id": "BN-1002",

        "symbol": "ETHUSDT",

        "status": "PENDING"

    },

    {

        "broker_order_id": "BN-1003",

        "symbol": "EURUSD",

        "status": "CANCELLED"

    }

]

sync.synchronize(broker_orders)

sync.print()

print()

print(sync.get_order("BN-1002"))