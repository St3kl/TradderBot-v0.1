from app.execution.order_router import OrderRouter

from app.execution.brokers.mock_broker import MockBroker

router = OrderRouter()

router.register(

    "Binance",

    MockBroker()

)

router.register(

    "MT5",

    MockBroker()

)

router.print()

print()

broker = router.route("Binance")

print(

    broker.place_order(

        {

            "symbol":"BTCUSDT"

        }

    )

)