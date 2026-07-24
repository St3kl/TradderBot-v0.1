from app.paper_trading.dashboard import PaperTradingDashboard

dashboard = PaperTradingDashboard()

dashboard.render(

    account={

        "balance":100450,

        "equity":100468,

        "floating_pnl":18

    },

    performance={

        "total_trades":3,

        "win_rate":66.67,

        "total_profit":180

    },

    current_signal={

        "symbol":"BTCUSDT",

        "signal":"BUY",

        "confidence":91

    },

    positions=[

        {

            "symbol":"BTCUSDT",

            "direction":"LONG",

            "entry":65000

        },

        {

            "symbol":"ETHUSDT",

            "direction":"LONG",

            "entry":3500

        }

    ]

)