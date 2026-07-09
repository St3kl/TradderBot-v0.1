from app.backtesting.backtest_engine import BacktestEngine


engine = BacktestEngine()

engine.run(

    symbol="BTCUSDT",

    timeframe="1h",

    start="2023-01-01",

    end="2023-12-31"

)