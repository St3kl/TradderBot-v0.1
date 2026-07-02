from app.smart_money.engine import analyze_smart_money


class SmartMoneyStage:

    def run(self, session):

        print("Running Smart Money Stage")

        session.smart_money = analyze_smart_money(
            opens=session.indicators["opens"],
            highs=session.indicators["highs"],
            lows=session.indicators["lows"],
            closes=session.indicators["closes"],
            current_price=session.indicators["price"],
            swing_high=session.sr["resistance"],
            swing_low=session.sr["support"]
        )

        return session