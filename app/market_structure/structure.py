from app.market_structure.swings import (
    find_swings
)

from app.market_structure.bos import (
    detect_bos
)

from app.market_structure.choch import (
    detect_choch
)

from app.market_structure.trend import (
    detect_trend
)


def analyze_structure(
    highs,
    lows,
    closes,
    bullish
):
    """
    Complete Market Structure Analysis.
    """

    swings = find_swings(
        highs,
        lows
    )

    trend = detect_trend(
        swings["highs"],
        swings["lows"]
    )

    bos = detect_bos(
        closes,
        swings["highs"],
        swings["lows"]
    )

    choch = detect_choch(
        closes,
        swings["highs"],
        swings["lows"],
        bullish
    )

    return {

        "trend": trend,

        "bos": bos,

        "choch": choch,

        "swing_highs": swings["highs"],

        "swing_lows": swings["lows"]

    }