from app.backtesting.replay_engine import ReplayEngine
from app.backtesting.candle_player import CandlePlayer

replay = ReplayEngine()

replay.load([
    {"close": 1},
    {"close": 2},
    {"close": 3},
])

player = CandlePlayer(replay)

for ctx in player.play():

    print(
        ctx.index,
        ctx.candle,
        ctx.previous,
        ctx.next,
    )