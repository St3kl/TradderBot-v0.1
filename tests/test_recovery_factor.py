from app.analytics.recovery_factor import RecoveryFactor

trades = [

    {

        "profit": 200,

        "drawdown": 100

    },

    {

        "profit": -50,

        "drawdown": 120

    },

    {

        "profit": 300,

        "drawdown": 80

    },

    {

        "profit": 150,

        "drawdown": 60

    }

]

engine = RecoveryFactor()

report = engine.analyze(trades)

engine.print(report)