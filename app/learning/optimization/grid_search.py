from itertools import product


class GridSearch:
    """
    Generates every possible parameter combination.
    """

    def generate(self, parameters):

        keys = list(parameters.keys())

        values = list(parameters.values())

        combinations = []

        for combo in product(*values):

            combinations.append(

                dict(zip(keys, combo))

            )

        return combinations