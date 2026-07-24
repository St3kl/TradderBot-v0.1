from app.paper_trading.trade_journal import TradeJournal

journal = TradeJournal()

journal.record({

    "symbol":"BTCUSDT",

    "strategy":"TREND",

    "profit":150

})

journal.record({

    "symbol":"ETHUSDT",

    "strategy":"BREAKOUT",

    "profit":-60

})

journal.record({

    "symbol":"EURUSD",

    "strategy":"RANGE",

    "profit":90

})

journal.print()