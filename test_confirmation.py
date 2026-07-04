from app.core.registry import engine
from app.execution.confirmation import ConfirmationEngine

session = engine.analyze("BTCUSDT")

confirmation = ConfirmationEngine()

print(

    confirmation.evaluate(session)

)