from app.smart_money.engine import (
    analyze_smart_money
)

opens = [100, 98, 105, 108, 106]

highs = [101, 106, 109, 109, 111]

lows = [97, 97, 104, 105, 105]

closes = [98, 105, 108, 106, 110]

result = analyze_smart_money(

    opens=opens,

    highs=highs,

    lows=lows,

    closes=closes,

    current_price=110,

    swing_high=111,

    swing_low=97

)

print(result)