from app.risk.position_sizing import calculate_position_size

result = calculate_position_size(
    balance=10000,
    risk_percent=1,
    entry=62500,
    stop_loss=62250
)

print(result)