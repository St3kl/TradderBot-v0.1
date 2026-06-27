from app.market_structure.structure import (
    analyze_structure
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

structure = analyze_structure(
    highs,
    lows,
    closes,
    bullish=True
)

print()

print(structure)