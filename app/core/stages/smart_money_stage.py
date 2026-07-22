from app.market.smart_money.engine import analyze_smart_money


class SmartMoneyStage:

    def run(self, session):

        print("Running Smart Money Stage")

        dataset = session.replay.dataset

        opens = [c["open"] for c in dataset]
        highs = [c["high"] for c in dataset]
        lows = [c["low"] for c in dataset]
        closes = [c["close"] for c in dataset]

        session.smart_money = analyze_smart_money(
            opens=opens,
            highs=highs,
            lows=lows,
            closes=closes,
            current_price=session.indicators["price"],
            swing_high=session.sr["resistance"],
            swing_low=session.sr["support"]
        )

        return session