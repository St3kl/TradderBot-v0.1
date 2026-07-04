from pprint import pprint

from app.core.registry import engine

from app.execution.execution_manager import ExecutionManager

from app.execution.report_builder import build_execution_report

session = engine.analyze("BTCUSDT")

manager = ExecutionManager()

portfolio = [

    {
        "symbol":"BTC",
        "direction":"LONG",
        "risk":100
    }

]

execution = manager.evaluate(

    session=session,

    balance=10000,

    risk_percent=1,

    open_positions=portfolio

)

report = build_execution_report(execution)

pprint(report)