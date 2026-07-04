class EntryEngine:

    def evaluate(self, session):

        trade = session.trade
        decision = session.decision

        if decision["action"] == "NO TRADE":

            return {

                "execute": False,

                "reason": "Trading engine rejected setup."

            }

        return {

            "execute": True,

            "entry": trade["entry"],

            "stop_loss": trade["stop_loss"],

            "take_profit": trade["take_profit"]

        }