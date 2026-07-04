from app.risk.risk_manager import RiskManager

manager = RiskManager()

trade = {

    "entry":62500,

    "stop_loss":62250

}

portfolio = [

    {

        "symbol":"BTC",

        "direction":"LONG",

        "risk":100

    },

    {

        "symbol":"ETH",

        "direction":"LONG",

        "risk":75

    },

    {

        "symbol":"SOL",

        "direction":"SHORT",

        "risk":50

    }

]

report = manager.evaluate(

    balance=10000,

    risk_percent=1,

    trade=trade,

    open_positions=portfolio

)

from pprint import pprint

pprint(report)