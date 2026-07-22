from app.backtesting.report_generator import ReportGenerator


portfolio = {

    "balance": 10850,

    "equity": 10850,

    "max_drawdown": 250

}

performance = {

    "win_rate": 62.5,

    "profit_factor": 2.14,

    "expectancy": 118

}

strategy = {

    "TREND": {

        "win_rate": 70

    }

}

market = {

    "TRENDING | NORMAL": {

        "win_rate": 65

    }

}

learning = {

    "strategy": "TREND",

    "confidence": 82,

    "reason": [

        "Trend performs best"

    ]

}

generator = ReportGenerator()

report = generator.generate(

    portfolio,

    performance,

    strategy,

    market,

    learning

)

generator.print(report)