from app.paper_trading.performance_metrics import PerformanceMetrics

engine = PerformanceMetrics()

trades = [

    {

        "profit":150

    },

    {

        "profit":-60

    },

    {

        "profit":90

    }

]

report = engine.calculate(trades)

engine.print(report)