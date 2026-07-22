class OrderExecutor:

    def execute(self, trade_plan):

        print()

        print("=" * 50)
        print("EXECUTING ORDER")
        print("=" * 50)

        print(f"Direction : {trade_plan.direction}")
        print(f"Entry     : {trade_plan.entry}")
        print(f"Stop      : {trade_plan.stop_loss}")
        print(f"Target    : {trade_plan.take_profit}")
        print(f"Size      : {trade_plan.position_size}")

        return {

            "status": "SIMULATED",

            "ticket": 1

        }