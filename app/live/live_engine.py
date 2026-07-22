from app.live.execution_validator import ExecutionValidator
from app.live.order_executor import OrderExecutor


class LiveEngine:

    def __init__(self):

        self.validator = ExecutionValidator()
        self.executor = OrderExecutor()

    def execute(self, session):

        if not self.validator.validate(session):

            print("Execution Cancelled")

            return None

        return self.executor.execute(

            session.trade_plan

        )