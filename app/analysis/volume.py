def analyze_volume(volumes):

    recent_volume = sum(
        volumes[-5:]
    ) / 5

    average_volume = sum(
        volumes[-50:]
    ) / 50

    ratio = (
        recent_volume /
        average_volume
    )

    if ratio >= 2:
        return {
            "strength": "Very High",
            "score": 100
        }

    if ratio >= 1.5:
        return {
            "strength": "High",
            "score": 80
        }

    if ratio >= 1:
        return {
            "strength": "Normal",
            "score": 60
        }

    return {
        "strength": "Weak",
        "score": 30
    }