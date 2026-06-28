from app.confluence.engine import (
    calculate_confluence
)

bullish = True

pattern = "Bullish Engulfing"

structure = {
    "trend": "Bullish",
    "bos": {
        "type": "Bullish BOS"
    }
}

volume = {
    "score": 18
}

alignment = 4

smart_money = {

    "order_blocks": {
        "bullish": [
            {
                "index": 10
            }
        ]
    },

    "fair_value_gaps": {
        "bullish": [
            {
                "index": 12
            }
        ]
    },

    "premium_discount": {
        "zone": "Discount"
    }

}

result = calculate_confluence(

    bullish,

    pattern,

    structure,

    volume,

    alignment,

    smart_money

)

print(result)