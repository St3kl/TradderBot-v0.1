from app.paper_trading.account_statistics import AccountStatistics

engine = AccountStatistics()

report = engine.calculate(

    starting_balance=100000,

    current_balance=100450,

    current_equity=100468,

    floating_pnl=18

)

engine.print(report)