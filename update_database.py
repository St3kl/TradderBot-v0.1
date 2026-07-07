from app.database.database import db

try:

    db.execute("""

    ALTER TABLE paper_trades
    ADD COLUMN strategy TEXT

    """)

    print("✓ Strategy column added.")

except Exception as e:

    print(e)