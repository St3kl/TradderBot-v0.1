from app.risk.calculator import calculate_trade_levels
from app.risk.position_sizer import PositionSizer


class TradeStage:

    def run(self, session):

        print("Running Trade Stage")
        
        if session.decision["action"] == "WAIT":

            print("Trade Stage -> WAIT")

            return session

        trade = calculate_trade_levels(
            price=session.indicators["price"],
            support=session.sr["support"],
            resistance=session.sr["resistance"],
            bullish=session.bullish,
            atr=session.indicators["atr"]
        )
        
        sizer = PositionSizer()

        
        balance = getattr(session, "balance", 10000)

        position = sizer.calculate(
            balance=balance,
            risk_percent=1,
            entry=trade["entry"],
            stop_loss=trade["stop_loss"],
        )

        trade["position_size"] = position["position_size"]
        trade["risk_amount"] = position["risk_amount"]

        # Store in the official session object
        session.trade_plan.entry = trade.get("entry")
        session.trade_plan.stop_loss = trade.get("stop_loss")
        session.trade_plan.take_profit = trade.get("take_profit")
        session.trade_plan.risk_reward = trade.get("risk_reward")

        session.trade_plan.position_size = trade.get("position_size")
        session.trade_plan.risk_amount = trade.get("risk_amount")

        # Temporary compatibility
        session.trade = trade

        print("Trade:", trade)

        return session