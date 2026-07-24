from app.execution.balance_synchronizer import BalanceSynchronizer

sync = BalanceSynchronizer()

sync.synchronize(

    balance=100250,

    equity=100275

)

sync.print()

print()

print(sync.get_balance())

print(sync.get_equity())