from app.database.database import db


class TradeRepository:

    def create_trade(self, trade):

        db.execute("""

        INSERT INTO paper_trades(

            symbol,
            direction,
            entry,
            stop_loss,
            take_profit,
            position_size,
            risk_amount,
            confidence,
            status,
            opened_at

        )

        VALUES(?,?,?,?,?,?,?,?,?,?)

        """, (

            trade["symbol"],
            trade["direction"],
            trade["entry"],
            trade["stop_loss"],
            trade["take_profit"],
            trade["position_size"],
            trade["risk_amount"],
            trade["confidence"],
            "OPEN",
            trade["opened_at"]

        ))

    def get_open_trades(self):

        rows = db.fetchall("""

        SELECT *

        FROM paper_trades

        WHERE status='OPEN'

        """)

        return [dict(r) for r in rows]

    def get_all_trades(self):

        rows = db.fetchall("""

        SELECT *

        FROM paper_trades

        ORDER BY id

        """)

        return [dict(r) for r in rows]

    def get_closed_trades(self):

        rows = db.fetchall("""

        SELECT *

        FROM paper_trades

        WHERE status='CLOSED'

        """)

        return [dict(r) for r in rows]

    def get_winning_trades(self):

        rows = db.fetchall("""

        SELECT *

        FROM paper_trades

        WHERE result='WIN'

        """)

        return [dict(r) for r in rows]

    def get_losing_trades(self):

        rows = db.fetchall("""

        SELECT *

        FROM paper_trades

        WHERE result='LOSS'

        """)

        return [dict(r) for r in rows]