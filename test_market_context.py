from pprint import pprint

from app.database.database import db

rows = db.fetchall("""

SELECT

    symbol,
    strategy,
    market_regime,
    volatility,
    session_name

FROM paper_trades

ORDER BY id DESC

LIMIT 5

""")

print("\n========== MARKET CONTEXT ==========\n")

for row in rows:

    pprint(dict(row))