from datetime import datetime, timedelta

from app.portfolio.execution_cooldown import ExecutionCooldown

engine = ExecutionCooldown()

now = datetime.utcnow()

history = [

    {

        "symbol":"BTCUSDT",

        "closed_at":now - timedelta(minutes=10)

    }

]

report = engine.check(

    "BTCUSDT",

    history,

    cooldown_minutes=30,

    now=now

)

engine.print(report)

print()

report = engine.check(

    "ETHUSDT",

    history,

    cooldown_minutes=30,

    now=now

)

engine.print(report)