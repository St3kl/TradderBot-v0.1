# from pprint import pprint

# from app.core.registry import engine

# from app.execution.execution_manager import ExecutionManager

# from app.paper.paper_engine import PaperTradingEngine

# session = engine.analyze("BTCUSDT")

# execution = ExecutionManager().evaluate(

#     session=session,

#     balance=10000,

#     risk_percent=1,

#     open_positions=[]

# )

# paper = PaperTradingEngine()

# trade = paper.open_trade(

#     session,

#     execution

# )

# pprint(trade)



from pprint import pprint

from app.core.registry import engine
from app.execution.execution_manager import ExecutionManager
from app.paper.paper_engine import PaperTradingEngine

session = engine.analyze("BTCUSDT")

execution = ExecutionManager().evaluate(

    session=session,

    balance=10000,

    risk_percent=1,

    open_positions=[]

)

print("\n========== EXECUTION ==========\n")
pprint(execution)

paper = PaperTradingEngine()

trade = paper.open_trade(
    session,
    execution
)

print("\n========== TRADE ==========\n")
pprint(trade)