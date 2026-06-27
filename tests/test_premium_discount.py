from app.smart_money.premium_discount import (
    premium_discount_zone
)

result = premium_discount_zone(

    current_price=175,

    swing_high=200,

    swing_low=100

)

print(result)