from app.history.backtest_archive import BacktestArchive

archive = BacktestArchive()

archive.save({

    "portfolio": {

        "balance": 10450

    },

    "performance": {

        "winrate": 62

    }

})

print(archive.latest())