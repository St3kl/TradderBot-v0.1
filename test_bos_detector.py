from app.market.structure.swing_detector import SwingDetector
from app.market.structure.bos_detector import BOSDetector

highs = [1,2,4,8,5,3,2,5,9,6,3]
lows  = [0,1,2,4,3,1,0,2,4,2,1]

# Price breaks above last swing high
closes = [1,2,3,4,5,6,7,8,9,10,11]

swings = SwingDetector()

high_points, low_points = swings.detect(
    highs,
    lows
)

bos = BOSDetector()

result = bos.detect(
    closes,
    high_points,
    low_points
)

print(result)