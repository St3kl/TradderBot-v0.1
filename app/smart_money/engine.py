from app.smart_money.liquidity import (
    detect_liquidity
)

from app.smart_money.order_blocks import (
    detect_order_blocks
)

from app.smart_money.fair_value_gap import (
    detect_fair_value_gaps
)

from app.smart_money.premium_discount import (
    premium_discount_zone
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

    return {

        "liquidity": liquidity,

        "order_blocks": order_blocks,

        "fair_value_gaps": fvg,

        "premium_discount": premium_discount

    }