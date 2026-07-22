from app.market.structure.swing_detector import SwingDetector
from app.market.structure.choch_detector import CHoCHDetector

highs = [1,2,4,8,5,3,2,5,9,6,3]
lows  = [0,1,2,4,3,1,0,2,4,2,1]

closes = [1,2,3,4,5,6,7,8,9,10,11]

detector = SwingDetector()

high_points, low_points = detector.detect(
    highs,
    lows
)

choch = CHoCHDetector()

result = choch.detect(

    closes=closes,

    swing_highs=high_points,

    swing_lows=low_points,

    current_trend="Bearish"

)

print(result)