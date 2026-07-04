from datetime import datetime

from pprint import pprint

from app.database.repositories.market_repository import MarketRepository

repo = MarketRepository()

repo.save_snapshot({

    "symbol":"BTCUSDT",

    "timestamp":datetime.utcnow().isoformat(),

    "price":62500,

    "trend":"Bullish",

    "confidence":85,

    "decision":"BUY"

})

history = repo.get_history("BTCUSDT")

pprint(history)