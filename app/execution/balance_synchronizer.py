class BalanceSynchronizer:

    def __init__(self):

        self.balance = 0.0
        self.equity = 0.0

    def synchronize(self, balance, equity=None):

        self.balance = balance

        if equity is None:
            equity = balance

        self.equity = equity

    def get_balance(self):

        return self.balance

    def get_equity(self):

        return self.equity

    def print(self):

        print()

        print("=" * 60)
        print("BALANCE SYNCHRONIZATION")
        print("=" * 60)
        print()

        print("Balance :", self.balance)
        print("Equity  :", self.equity)