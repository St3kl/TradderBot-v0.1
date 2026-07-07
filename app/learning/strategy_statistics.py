from app.database.database import db


class StrategyStatistics:

    def summary(self):

        rows = db.fetchall("""

        SELECT

            strategy,

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

        WHERE strategy IS NOT NULL

        GROUP BY strategy

        """)

        report = {}

        for row in rows:

            total = row["total"]

            wins = row["wins"] or 0

            losses = row["losses"] or 0

            if total:

                win_rate = round(
                    wins / total * 100,
                    2
                )

            else:

                win_rate = 0

            report[row["strategy"]] = {

                "wins": wins,

                "losses": losses,

                "total": total,

                "win_rate": win_rate

            }

        return report