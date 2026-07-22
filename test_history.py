from app.backtesting.replay_engine import ReplayEngine
from app.backtesting.candle_player import CandlePlayer

candles = []

for i in range(5):

    candles.append({
        "time": i,
        "close": i
    })

replay = ReplayEngine()

replay.load(candles, "BTCUSDT")

player = CandlePlayer(replay)

for context in player.play():

    print(
        context.index,
        len(context.history)
    )
    
    # python run_backtest.py