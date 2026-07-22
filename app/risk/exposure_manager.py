class ExposureManager:

    """
    Prevents excessive portfolio exposure.
    """

    def __init__(self):

        self.max_positions = 5

    def evaluate(self, open_positions):

        total = len(open_positions)

        if total >= self.max_positions:

            return {

                "allowed": False,

                "reason": "Maximum exposure reached"

            }

        return {

            "allowed": True,

            "reason": ""

        }