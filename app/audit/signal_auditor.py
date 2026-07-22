class SignalAuditor:

    def audit(self, session):

        checks = {

            "EMA Trend": session.trend.get("bullish", False),

            "Market Structure":
                session.structure.trend == "Bullish",

            "Bullish BOS":
                session.structure.bullish_bos,

            "Bullish CHoCH":
                session.structure.bullish_choch,

            "Discount Zone":
                session.smart_money["premium_discount"]["zone"] == "Discount",

            "Order Block":
                session.smart_money["order_blocks"]["bullish"] > 0,

            "Fair Value Gap":
                session.smart_money["fair_value_gaps"]["bullish"] > 0,

            "Liquidity Sweep":
                session.smart_money["liquidity_sweep"]["sell_side"],

            "Strong Volume":
                session.volume["score"] >= 70,

            "Risk Reward":
                session.trade_plan.risk_reward >= 2,

        }

        return checks