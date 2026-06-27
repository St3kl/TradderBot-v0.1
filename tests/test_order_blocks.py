from app.smart_money.order_blocks import (
    detect_order_blocks
)

opens = [

    100,
    98,
    105,
    108,
    106

]

closes = [

    98,
    105,
    108,
    106,
    110

]

highs = [

    101,
    106,
    109,
    109,
    111

]

lows = [

    97,
    97,
    104,
    105,
    105

]

blocks = detect_order_blocks(

    opens,
    highs,
    lows,
    closes

)

print(blocks)