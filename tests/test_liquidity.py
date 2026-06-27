from app.smart_money.liquidity import (
    detect_liquidity
)

highs = [

    100,

    103,

    110,

    110.05,

    107,

    112

]

lows = [

    90,

    88,

    84,

    84.02,

    86,

    91

]

result = detect_liquidity(
    highs,
    lows
)

print(result)