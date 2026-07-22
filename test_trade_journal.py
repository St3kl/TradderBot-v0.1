from app.history.trade_journal import TradeJournal

journal = TradeJournal()

journal.save({

    "time": "2026-07-20",

    "symbol": "BTCUSDT",

    "strategy": "TREND",

    "direction": "LONG",

    "entry": 100,

    "exit": 110,

    "stop_loss": 95,

    "take_profit": 110,

    "risk_reward": 2,

    "position_size": 1,

    "profit": 10,

    "result": "WIN",

    "confidence": 85,

})

print("Trade saved.")