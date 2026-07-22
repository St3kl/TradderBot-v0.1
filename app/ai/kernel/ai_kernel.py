from app.learning.learning_engine import LearningEngine
from app.ai.brain.decision_brain import DecisionBrain


class AIKernel:
    """
    Central AI interface.

    Every AI interaction goes through this class.
    """

    def __init__(self):

        self.learning = LearningEngine()

        self.brain = DecisionBrain()

    # -----------------------------
    # Learn
    # -----------------------------

    def learn(self, trade):

        return self.learning.learn(trade)

    # -----------------------------
    # Think
    # -----------------------------

    def think(

        self,

        strategy,

        context,

        confidence,

        risk

    ):

        return self.brain.think(

            strategy,

            context,

            confidence,

            risk

        )