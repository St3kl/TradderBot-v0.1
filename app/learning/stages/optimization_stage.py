class OptimizationStage:
    """
    Converts learning recommendations into
    optimized trading parameters.
    """

    def process(self, recommendation):

        optimized = {

            "preferred_strategy":
                recommendation["strategy"],

            "preferred_market":
                recommendation["market"],

            "minimum_confidence":
                recommendation["confidence"],

            "risk_percent":
                self._risk(recommendation),

            "risk_reward":
                self._risk_reward(recommendation),

            "max_open_positions":
                self._positions(recommendation),

            "enabled": True,

            "notes":
                recommendation["notes"]

        }

        return optimized

    # ------------------------------------------

    def _risk(self, recommendation):

        confidence = recommendation["confidence"]

        if confidence is None:

            return 1.0

        if isinstance(confidence, str):

            confidence = int(confidence.replace("%", ""))

        if confidence >= 95:

            return 2.0

        if confidence >= 90:

            return 1.5

        if confidence >= 80:

            return 1.0

        return 0.5

    # ------------------------------------------

    def _risk_reward(self, recommendation):

        confidence = recommendation["confidence"]

        if confidence is None:

            return 2.0

        if confidence >= 95:

            return 3.0

        if confidence >= 90:

            return 2.5

        return 2.0

    # ------------------------------------------

    def _positions(self, recommendation):

        confidence = recommendation["confidence"]

        if confidence is None:

            return 1

        if confidence >= 95:

            return 3

        if confidence >= 90:

            return 2

        return 1
    
    
    
   