from datetime import datetime, timedelta


class TradeExpiration:

    def filter(self, trades, now=None):

        if now is None:
            now = datetime.utcnow()

        valid = []
        expired = []

        for trade in trades:

            created = trade["created_at"]
            ttl = trade.get("ttl_minutes", 30)

            if now <= created + timedelta(minutes=ttl):
                valid.append(trade)
            else:
                expired.append(trade)

        return {

            "valid": valid,

            "expired": expired

        }

    def print(self, report):

        print()

        print("=" * 60)
        print("TRADE EXPIRATION")
        print("=" * 60)
        print()

        print("Valid")

        for trade in report["valid"]:

            print(

                f"{trade['symbol']:<12}"

                f"{trade['strategy']}"

            )

        print()

        print("Expired")

        for trade in report["expired"]:

            print(

                f"{trade['symbol']:<12}"

                f"{trade['strategy']}"

            )