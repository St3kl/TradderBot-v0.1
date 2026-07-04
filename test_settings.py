from app.config.settings import settings

print(

    settings.get(

        "risk",

        "risk_per_trade"

    )

)

print(

    settings.get(

        "account",

        "balance"

    )

)