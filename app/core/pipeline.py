class TradingPipeline:

    def __init__(self):

        self.steps = []

    def add_step(self, step):

        self.steps.append(step)

    def run(self, session):

        for step in self.steps:

            session = step.run(session)

        return session