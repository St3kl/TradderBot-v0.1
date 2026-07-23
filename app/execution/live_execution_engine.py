class LiveExecutionEngine:

    def __init__(

        self,

        router,

        connection_manager,

        retry_engine,

        latency_monitor,

        slippage_controller,

        health_monitor,

    ):

        self.router = router

        self.connection = connection_manager

        self.retry = retry_engine

        self.latency = latency_monitor

        self.slippage = slippage_controller

        self.health = health_monitor

    def execute(

        self,

        broker_name,

        order,

    ):

        broker = self.router.route(broker_name)

        self.connection.ensure_connection()

        latency = self.latency.measure(

            broker.place_order,

            order,

        )

        result = latency["result"]

        report = {

            "success": result["success"],

            "broker_order_id": result["broker_order_id"],

            "latency_ms": latency["latency_ms"]

        }

        return report

    def print(self, report):

        print()

        print("=" * 60)

        print("LIVE EXECUTION")

        print("=" * 60)

        print()

        print("Success        :", report["success"])

        print("Broker OrderID :", report["broker_order_id"])

        print("Latency        :", report["latency_ms"], "ms")