from app.smart_money.fair_value_gap import (
    detect_fair_value_gaps
)

highs = [

    100,
    108,
    111,
    115,
    116

]

lows = [

    95,
    101,
    105,
    112,
    114

]

result = detect_fair_value_gaps(
    highs,
    lows
)

print(result)