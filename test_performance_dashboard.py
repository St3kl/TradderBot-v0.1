from app.analytics.performance_dashboard import PerformanceDashboard

dashboard = PerformanceDashboard()

trades = [

    {"result": "WIN", "profit": 120},

    {"result": "LOSS", "profit": -100},

    {"result": "WIN", "profit": 200},

    {"result": "LOSS", "profit": -50},

]

print(dashboard.summarize(trades))