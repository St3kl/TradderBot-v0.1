from app.analytics.backtest_comparator import BacktestComparator

old_report = {

    "portfolio": {
        "balance": 10000
    },

    "performance": {
        "winrate": 55
    }

}

new_report = {

    "portfolio": {
        "balance": 10450
    },

    "performance": {
        "winrate": 62
    }

}

engine = BacktestComparator()

result = engine.compare(old_report, new_report)

engine.print(result)