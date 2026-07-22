from app.application import Application
from app.debug.pipeline_debugger import PipelineDebugger


def main():

    app = Application()

    result = app.backtest.run(
        symbol="BTCUSDT",
        timeframe="1H",
        start="2024-01-01",
        end="2024-12-31"
    )

    session = result["session"]

    debugger = PipelineDebugger()
    debugger.print_session(session)
    
    if result["session"].decision["action"] != "WAIT":

        app.application.live.execute(

        result["session"]

    )


if __name__ == "__main__":
    main()
    
    