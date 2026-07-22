class ParameterOptimizer:
    """
    Finds the best parameter based on
    historical performance.
    """

    def optimize(

        self,

        results,

        metric="win_rate"

    ):

        if not results:

            return None

        best = max(

            results,

            key=lambda x: x[metric]

        )

        return best