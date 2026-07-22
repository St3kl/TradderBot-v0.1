from app.dashboard.performance_dashboard import PerformanceDashboard

dashboard = PerformanceDashboard()

data = dashboard.build(

    portfolio={

        "balance": 10250,

        "max_drawdown": 2.1

    },

    analytics={

        "expectancy": 1.45,

        "winrate": 61

    },

    trade_quality={

        "score": 87,

        "grade": "A"

    },

    market_health={

        "score": 82

    },

    rejection_stats={

        "Low Confidence": {

            "count": 12

        }

    }

)

dashboard.print(data)