from app.database.database import db


def create_tables():

    db.execute("""

    CREATE TABLE IF NOT EXISTS market_snapshots(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        symbol TEXT,

        timestamp TEXT,

        price REAL,

        trend TEXT,

        confidence INTEGER,

        decision TEXT

    )

    """)

    db.execute("""

    CREATE TABLE IF NOT EXISTS paper_trades(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        symbol TEXT,

        entry REAL,

        stop_loss REAL,

        take_profit REAL,

        position_size REAL,

        status TEXT,

        pnl REAL,

        opened_at TEXT,

        closed_at TEXT

    )

    """)