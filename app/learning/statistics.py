from app.database.database import db


class Statistics:

    def total_trades(self):

        row = db.fetchone("""

        SELECT COUNT(*) AS total

        FROM paper_trades

        """)

        return row["total"]

    def wins(self):

        row = db.fetchone("""

        SELECT COUNT(*) AS wins

        FROM paper_trades

        WHERE result='WIN'

        """)

        return row["wins"]

    def losses(self):

        row = db.fetchone("""

        SELECT COUNT(*) AS losses

        FROM paper_trades

        WHERE result='LOSS'

        """)

        return row["losses"]