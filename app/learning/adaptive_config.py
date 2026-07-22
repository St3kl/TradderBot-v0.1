class AdaptiveConfig:
    """
    Stores the latest optimized trading parameters.

    This object is shared across the application so
    every new analysis can use the latest learning.
    """

    def __init__(self):

        self.reset()

    # --------------------------------------------

    def reset(self):

        self.data = {

            "preferred_strategy": None,

            "preferred_market": None,

            "minimum_confidence": 80,

            "risk_percent": 1.0,

            "risk_reward": 2.0,

            "max_open_positions": 1,

            "enabled": False

        }

    # --------------------------------------------

    def update(self, optimized):

        self.data.update(optimized)

    # --------------------------------------------

    def get(self):

        return self.data