from app.risk.position_sizer import PositionSizer

sizer = PositionSizer()

result = sizer.calculate(
    balance=10000,
    risk_percent=1,
    entry=64000,
    stop_loss=63800,
)

print(result)