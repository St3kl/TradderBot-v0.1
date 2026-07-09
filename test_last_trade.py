from pprint import pprint

from app.database.database import db

row = db.fetchall("""

SELECT *

FROM paper_trades

ORDER BY id DESC

LIMIT 1

""")

print("\n========== LAST TRADE ==========\n")

if row:
    pprint(dict(row[0]))
else:
    print("No trades found.")