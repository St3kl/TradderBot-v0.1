from pprint import pprint

from app.backtesting.performance_analyzer import PerformanceAnalyzer

trades = [

    {

        "result": "WIN",

        "pnl": 300

    },

    {

        "result": "LOSS",

        "pnl": -100

    },

    {

        "result": "WIN",

        "pnl": 250

    },

    {

        "result": "LOSS",

        "pnl": -150

    }

]

report = PerformanceAnalyzer().analyze(trades)

pprint(report)