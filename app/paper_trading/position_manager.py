class PositionManager:

    def __init__(self):

        self.positions = []

    def add(self, position):

        self.positions.append(position)

    def open_positions(self):

        return [

            p

            for p in self.positions

            if p["status"] == "OPEN"

        ]

    def closed_positions(self):

        return [

            p

            for p in self.positions

            if p["status"] == "CLOSED"

        ]

    def get(self, broker_order_id):

        for position in self.positions:

            if position["broker_order_id"] == broker_order_id:

                return position

        return None

    def summary(self):

        return {

            "total": len(self.positions),

            "open": len(self.open_positions()),

            "closed": len(self.closed_positions())

        }

    def print(self):

        s = self.summary()

        print()

        print("=" * 60)

        print("POSITION MANAGER")

        print("=" * 60)

        print()

        print("Total  :", s["total"])

        print("Open   :", s["open"])

        print("Closed :", s["closed"])