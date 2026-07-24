from app.paper_trading.equity_engine import EquityEngine

engine = EquityEngine()

positions = [

    {

        "unrealized_pnl": 12.5

    },

    {

        "unrealized_pnl": -3

    },

    {

        "unrealized_pnl": 8.2

    }

]

report = engine.calculate(

    balance=100000,

    unrealized_positions=positions

)

engine.print(report)