from app.portfolio.portfolio_governor import PortfolioGovernor

engine = PortfolioGovernor()

report = engine.approve(

    risk_mode={

        "mode":"NORMAL"

    },

    strategy_health={

        "status":"HEALTHY"

    },

    portfolio_risk={

        "level":"MODERATE"

    },

    trading_window={

        "allowed":True,

        "reasons":[]

    }

)

engine.print(report)

print()

report = engine.approve(

    risk_mode={

        "mode":"SURVIVAL"

    },

    strategy_health={

        "status":"CRITICAL"

    },

    portfolio_risk={

        "level":"CRITICAL"

    },

    trading_window={

        "allowed":False,

        "reasons":[

            "Market Closed"

        ]

    }

)

engine.print(report)