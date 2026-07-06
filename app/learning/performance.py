from app.database.database import db


class Performance:

    def average_pnl(self):

        row = db.fetchone("""

        SELECT AVG(pnl) AS avg_pnl

        FROM paper_trades

        WHERE pnl IS NOT NULL

        """)

        return row["avg_pnl"] or 0

    def total_pnl(self):

        row = db.fetchone("""

        SELECT SUM(pnl) AS total

        FROM paper_trades

        WHERE pnl IS NOT NULL

        """)

        return row["total"] or 0