from app.database.database import db


class MarketStatistics:
    """
    Learns how the bot performs under different market regimes.
    """

    def update(self, trade):

        print("Updating Market Statistics")

    def summary(self):

        rows = db.fetchall("""

        SELECT

            market_regime,

            volatility,

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

        WHERE market_regime IS NOT NULL

        GROUP BY market_regime, volatility

        ORDER BY market_regime

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

            key = f"{row['market_regime']} | {row['volatility']}"

            report[key] = {

                "wins": wins,

                "losses": losses,

                "total": total,

                "win_rate": win_rate

            }

        return report