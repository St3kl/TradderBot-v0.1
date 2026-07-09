from app.database.database import db
import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )
)


def migrate():

    columns = [

        ("market_regime", "TEXT"),

        ("volatility", "TEXT"),

        ("session_name", "TEXT")

    ]

    existing = [

        row["name"]

        for row in db.fetchall(

            "PRAGMA table_info(paper_trades)"

        )

    ]

    for name, datatype in columns:

        if name not in existing:

            db.execute(

                f"ALTER TABLE paper_trades ADD COLUMN {name} {datatype}"

            )

            print(f"✓ Added column: {name}")


if __name__ == "__main__":

    migrate()