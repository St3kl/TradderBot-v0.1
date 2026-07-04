from app.database.database import db

rows = db.fetchall("PRAGMA table_info(paper_trades)")

for row in rows:
    print(dict(row))