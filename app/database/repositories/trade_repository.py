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

        """,(

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