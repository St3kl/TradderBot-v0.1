from app.strategy.strategy_selector import StrategySelector

selector = StrategySelector()

print(

    selector.select(

        {

            "regime": "TRENDING"

        }

    )

)