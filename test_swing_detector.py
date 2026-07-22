from app.market.structure.swing_detector import SwingDetector

highs = [1,2,4,8,5,3,2,5,9,6,3]
lows  = [0,1,2,4,3,1,0,2,4,2,1]

detector = SwingDetector()

high_points, low_points = detector.detect(
    highs,
    lows
)

print("Swing Highs")

for s in high_points:
    print(s)

print()

print("Swing Lows")

for s in low_points:
    print(s)