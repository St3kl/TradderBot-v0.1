from app.risk.calculator import calculate_trade_levels


class TradeStage:

    def run(self, session):

        print("Running Trade Stage")

        session.trade = calculate_trade_levels(
            price=session.indicators["price"],
            support=session.sr["support"],
            resistance=session.sr["resistance"],
            bullish=session.bullish,
            atr=session.indicators["atr"]
        )

        print("Trade:", session.trade)

        return session