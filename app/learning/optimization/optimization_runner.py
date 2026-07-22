class OptimizationRunner:
    """
    Executes optimization jobs.

    For every parameter combination:

    - Backtest
    - Walk Forward
    - Monte Carlo
    - Score
    """

    def __init__(self):

        self.results = []

    def run(

        self,

        parameter_sets,

        evaluator

    ):

        self.results.clear()

        for parameters in parameter_sets:

            result = evaluator(parameters)

            self.results.append(result)

        return self.results