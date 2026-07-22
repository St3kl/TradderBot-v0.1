import random


class MonteCarloSimulator:
    """
    Runs Monte Carlo simulations by randomizing
    the order of historical trade results.
    """

    def simulate(

        self,

        trades,

        iterations=1000

    ):

        if not trades:

            return []

        simulations = []

        for _ in range(iterations):

            shuffled = trades.copy()

            random.shuffle(shuffled)

            balance = 0

            equity = []

            for trade in shuffled:

                balance += trade["pnl"]

                equity.append(balance)

            simulations.append(equity)

        return simulations