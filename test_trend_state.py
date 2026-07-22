from app.market.structure.trend_state import TrendState

engine = TrendState()

bos = {

    "bullish": True,

    "bearish": False

}

choch = {

    "bullish": False,

    "bearish": False

}

print(

    engine.evaluate(

        bos,

        choch

    )

)