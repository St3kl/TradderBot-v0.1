from app.market.candle_builder import CandleBuilder

builder = CandleBuilder()

prices = [

    65000,

    65030,

    64980,

    65070,

    65040

]

for p in prices:

    builder.update(

        p,

        volume=2

    )

builder.print()

print()

print(builder.get_candle())