from app.market.tick_aggregator import TickAggregator

agg = TickAggregator()

agg.add_tick(65000, volume=1.2)

agg.add_tick(65020, volume=0.8)

agg.add_tick(64990, volume=1.5)

agg.print()

print()

print(agg.all())

print()

agg.clear()

print("After Clear:", agg.count())