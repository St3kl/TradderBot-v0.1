from app.market_structure.swings import (
    find_swings
)

from app.market_structure.bos import (
    detect_bos
)

highs = [
    1,2,3,6,4,3,5,8,6,5
]

lows = [
    1,1,2,4,2,1,3,4,3,2
]

closes = [
    1,2,3,5,4,3,5,8,7,9
]

swings = find_swings(
    highs,
    lows
)

bos = detect_bos(
    closes,
    swings["highs"],
    swings["lows"]
)

print(bos)