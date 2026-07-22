from app.market.smart_money.liquidity import (
    detect_liquidity
)

from app.market.smart_money.order_blocks import (
    detect_order_blocks
)

from app.market.smart_money.fair_value_gap import (
    detect_fair_value_gaps
)

from app.market.smart_money.premium_discount import (
    premium_discount_zone
)

from app.market.smart_money.liquidity_sweep import (
    detect_liquidity_sweep
)


def analyze_smart_money(
    opens,
    highs,
    lows,
    closes,
    current_price,
    swing_high,
    swing_low
):
    """
    Run all Smart Money analyses.
    """

    liquidity = detect_liquidity(
        highs,
        lows
    )

    order_blocks = detect_order_blocks(
        opens,
        highs,
        lows,
        closes
    )

    fvg = detect_fair_value_gaps(
        highs,
        lows
    )

    premium_discount = premium_discount_zone(
        current_price,
        swing_high,
        swing_low
    )

    liquidity_sweep = detect_liquidity_sweep(
        highs,
        lows,
        closes
    )

    return {

        "liquidity": {

            "equal_highs": len(liquidity["equal_highs"]),

            "equal_lows": len(liquidity["equal_lows"])

        },

        "order_blocks": {

            "bullish": len(order_blocks["bullish"]),

            "bearish": len(order_blocks["bearish"])

        },

        "fair_value_gaps": {

            "bullish": len(fvg["bullish"]),

            "bearish": len(fvg["bearish"])

        },

        "premium_discount": premium_discount,

        "liquidity_sweep": liquidity_sweep

    }