class LearningListener:

    def __init__(self, learning_engine):

        self.learning = learning_engine

    def handle(self, trade):

        print("Learning Listener")

        self.learning.learn(trade)