from datetime import datetime


class OrderIDManager:

    def __init__(self):

        self.counter = 0

    def generate(self):

        self.counter += 1

        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")

        return f"TB-{timestamp}-{self.counter:06d}"

    def reset(self):

        self.counter = 0