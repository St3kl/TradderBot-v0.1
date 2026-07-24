from app.safety.production_readiness_validator import (
    ProductionReadinessValidator
)

validator = ProductionReadinessValidator()

# Healthy configuration

result = validator.validate(

    kill_switch_active=False,

    circuit_open=False,

    health_score=95,

    production_mode_live=True,

    broker_connected=True

)

validator.print(result)

print()

# Unsafe configuration

result = validator.validate(

    kill_switch_active=True,

    circuit_open=True,

    health_score=65,

    production_mode_live=False,

    broker_connected=False

)

validator.print(result)