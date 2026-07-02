# from app.risk.calculator import calculate_trade_levels


# class TradeStage:

#     def run(self, session):

#         print("Running Trade Stage")

#         session.trade = calculate_trade_levels(
#             price=session.indicators["price"],
#             support=session.sr["support"],
#             resistance=session.sr["resistance"],
#             bullish=session.bullish,
#             atr=session.indicators["atr"]
#         )

#         return session

class TrendStage:

    def run(self, session):

        print("Running Trend Stage")

        session.bullish = (
            session.indicators["ema50"]
            >
            session.indicators["ema200"]
        )

        return session