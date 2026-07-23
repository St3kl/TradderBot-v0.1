from app.execution.brokers.mock_broker import MockBroker

from app.execution.order_router import OrderRouter

from app.execution.retry_engine import RetryEngine

from app.execution.latency_monitor import LatencyMonitor

from app.execution.slippage_controller import SlippageController

from app.execution.broker_health_monitor import BrokerHealthMonitor

from app.execution.broker_connection_manager import BrokerConnectionManager

from app.execution.live_execution_engine import LiveExecutionEngine


broker = MockBroker()

broker.connect()

router = OrderRouter()

router.register("Binance", broker)

connection = BrokerConnectionManager(broker)

retry = RetryEngine()

latency = LatencyMonitor()

slippage = SlippageController()

health = BrokerHealthMonitor()

engine = LiveExecutionEngine(

    router,

    connection,

    retry,

    latency,

    slippage,

    health,

)

report = engine.execute(

    "Binance",

    {

        "symbol":"BTCUSDT",

        "direction":"LONG",

        "quantity":0.02

    }

)

engine.print(report)