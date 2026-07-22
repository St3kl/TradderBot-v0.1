from app.risk.risk_manager import RiskManager


class Session:
    pass


session = Session()

session.market_health = {

    "score": 80

}

session.volatility = {

    "level": "NORMAL"

}

session.correlation = {

    "score": 75

}


portfolio = {

    "max_drawdown": 5,

    "daily_loss_percent": 1

}


positions = [

    {

        "risk_percent": 1

    }

]

manager = RiskManager()

print(

    manager.evaluate(

        session,

        portfolio,

        positions

    )

)