from app.database.database import db


class MarketRepository:

    def save_snapshot(self, snapshot):

        db.execute("""

        INSERT INTO market_snapshots(

            symbol,

            timestamp,

            price,

            trend,

            confidence,

            decision

        )

        VALUES(?,?,?,?,?,?)

        """, (

            snapshot["symbol"],

            snapshot["timestamp"],

            snapshot["price"],

            snapshot["trend"],

            snapshot["confidence"],

            snapshot["decision"]

        ))

    def get_history(self, symbol):

        rows = db.fetchall("""

        SELECT *

        FROM market_snapshots

        WHERE symbol=?

        ORDER BY id

        """, (symbol,))

        return [dict(r) for r in rows]