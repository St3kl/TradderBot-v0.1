from datetime import datetime, UTC

datetime.now(UTC)

from app.paper_trading.live_paper_loop import LivePaperTradingLoop


def analyzer():

    return {

        "signal": "BUY",

        "symbol": "BTCUSDT",

        "confidence": 91,

        "time": str(datetime.now(UTC))


    }


engine = LivePaperTradingLoop(

    analyzer,

    interval=1

)

engine.start(

    iterations=3

)