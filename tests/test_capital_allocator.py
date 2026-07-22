from app.ranking.capital_allocator import CapitalAllocator

allocator = CapitalAllocator()

for score in [95, 85, 75, 65, 40]:

    result = allocator.allocate(
        {"score": score},
        balance=10000
    )

    print(score, result)