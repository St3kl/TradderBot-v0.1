def classify_volatility(atr):

    if atr < 100:
        return "Low"

    elif atr < 300:
        return "Medium"

    else:
        return "High"