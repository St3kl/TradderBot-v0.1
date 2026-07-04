import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)

DB_FILE = DATA_DIR / "tradderbot.db"


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(DB_FILE)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):

        self.cursor.execute(query, params)

        self.connection.commit()

    def fetchall(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchall()

    def fetchone(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchone()

    def close(self):

        self.connection.close()


db = Database()