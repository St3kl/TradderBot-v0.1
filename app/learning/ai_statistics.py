from app.database.database import db


class AIStatistics:
    """
    Learns how AI confidence performs over time.
    """

    def update(self, trade):

        print("Updating AI Statistics")

    def summary(self):

        rows = db.fetchall("""

        SELECT

            ROUND(confidence, -1) AS confidence_group,

            COUNT(*) AS total,

            SUM(
                CASE
                    WHEN result='WIN'
                    THEN 1
                    ELSE 0
                END
            ) AS wins,

            SUM(
                CASE
                    WHEN result='LOSS'
                    THEN 1
                    ELSE 0
                END
            ) AS losses

        FROM paper_trades

        WHERE confidence IS NOT NULL

        GROUP BY confidence_group

        ORDER BY confidence_group DESC

        """)

        report = {}

        for row in rows:

            total = row["total"]

            wins = row["wins"] or 0

            losses = row["losses"] or 0

            win_rate = round(
                (wins / total) * 100,
                2
            ) if total else 0

            report[f"{row['confidence_group']}%"] = {

                "wins": wins,

                "losses": losses,

                "total": total,

                "win_rate": win_rate

            }

        return report