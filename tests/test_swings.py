from app.market_structure.swings import (
    find_swings
)

highs = [
    1,2,3,6,4,3,5,8,6,5
]

lows = [
    1,1,2,4,2,1,3,4,3,2
]

swings = find_swings(
    highs,
    lows
)

print(swings)