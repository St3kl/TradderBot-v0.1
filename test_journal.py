from pprint import pprint

from app.core.registry import engine
from app.journal.journal_engine import JournalEngine

session = engine.analyze("BTCUSDT")

journal = JournalEngine()

entry = journal.build_entry(session)

pprint(entry)