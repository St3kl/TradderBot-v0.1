from app.execution.slippage_controller import SlippageController

engine = SlippageController()

report = engine.calculate(

    requested_price=65000,

    executed_price=65018

)

engine.print(report)

print()

print(

    "Acceptable:",

    engine.acceptable(

        report,

        max_slippage=25

    )

)

print(

    "Acceptable:",

    engine.acceptable(

        report,

        max_slippage=10

    )

)