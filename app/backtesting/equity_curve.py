class EquityCurve:
    """
    Tracks the account equity after every closed trade.
    """

    def __init__(self):

        self.points = []

    def add(self, balance):

        self.points.append(balance)

    def get(self):

        return self.points

    def reset(self):

        self.points.clear()