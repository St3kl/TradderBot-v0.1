from app.core.registry import engine
from app.execution.execution_manager import ExecutionManager

session = engine.analyze("BTCUSDT")

manager = ExecutionManager()

portfolio = [

    {
        "symbol":"BTC",
        "direction":"LONG",
        "risk":100
    }

]

report = manager.evaluate(

    session=session,

    balance=10000,

    risk_percent=1,

    open_positions=portfolio

)

from pprint import pprint

pprint(report)