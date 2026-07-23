from app.portfolio.trade_queue import TradeQueue

queue = TradeQueue()

queue.add({

    "symbol":"BTCUSDT",

    "strategy":"TREND",

    "confidence":82

})

queue.add({

    "symbol":"ETHUSDT",

    "strategy":"BREAKOUT",

    "confidence":91

})

queue.add({

    "symbol":"EURUSD",

    "strategy":"RANGE",

    "confidence":74

})

queue.print()

print()

print("Executing...")

print(queue.pop())

print()

queue.print()