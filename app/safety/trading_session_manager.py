from datetime import datetime, UTC


class TradingSessionManager:

    def __init__(self):

        self.sessions = {

            "LONDON": (7, 16),

            "NEW_YORK": (13, 22),

            "ASIA": (0, 9),

            "CRYPTO": (0, 24)

        }

    def is_open(self, session):

        session = session.upper()

        if session not in self.sessions:
            return False

        start, end = self.sessions[session]

        hour = datetime.now(UTC).hour

        return start <= hour < end

    def print(self, session):

        print()

        print("=" * 60)
        print("TRADING SESSION")
        print("=" * 60)
        print()

        print("Session :", session.upper())
        print("Open    :", self.is_open(session))