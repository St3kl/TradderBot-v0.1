from app.portfolio.execution_scheduler import ExecutionScheduler

scheduler = ExecutionScheduler(max_positions=2)

queue = [

    {"symbol":"BTCUSDT","priority":95},

    {"symbol":"ETHUSDT","priority":91},

    {"symbol":"EURUSD","priority":83},

    {"symbol":"XAUUSD","priority":80},

]

scheduled = scheduler.schedule(

    queue,

    open_positions=0

)

scheduler.print(scheduled)