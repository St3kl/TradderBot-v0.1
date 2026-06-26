from app.market_structure.swings import find_swings
from app.market_structure.choch import detect_choch

highs = [
    1,2,3,6,4,3,5,8,6,5
]

lows = [
    1,1,2,4,2,1,3,4,3,2
]

closes = [
    1,2,3,6,4,3,5,8,6,0.5
]

swings = find_swings(
    highs,
    lows
)

choch = detect_choch(
    closes,
    swings["highs"],
    swings["lows"],
    bullish=True
)

print(choch)