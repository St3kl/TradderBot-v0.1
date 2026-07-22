from app.risk.drawdown_guard import DrawdownGuard

guard = DrawdownGuard()

portfolio = {
    "max_drawdown": 5
}

print(guard.evaluate(portfolio))

portfolio = {
    "max_drawdown": 12
}

print(guard.evaluate(portfolio))