from app.risk.daily_loss_guard import DailyLossGuard

guard = DailyLossGuard()

portfolio = {

    "daily_loss_percent": 1.5

}

print(guard.evaluate(portfolio))

portfolio = {

    "daily_loss_percent": 3.8

}

print(guard.evaluate(portfolio))