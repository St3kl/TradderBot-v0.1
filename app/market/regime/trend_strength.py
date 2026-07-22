def classify_adx(adx):

    if adx < 20:
        return "Weak"

    elif adx < 25:
        return "Developing"

    elif adx < 40:
        return "Strong"

    else:
        return "Very Strong"