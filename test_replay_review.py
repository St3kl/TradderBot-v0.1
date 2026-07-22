from app.replay.replay_review import ReplayReview


class Dummy:

    pass


session = Dummy()

session.decision = {
    "action": "WAIT",
    "reason": "Low Confidence",
    "confidence": 42
}

session.confluence = {
    "score": 45,
    "signals": [
        "Order Block",
        "FVG"
    ],
    "missing": [
        "EMA Trend",
        "Volume"
    ]
}

session.validation = {
    "score": 60
}

session.checklist = {
    "EMA Trend": False,
    "Order Block": True,
    "FVG": True,
    "Volume": False
}

review = ReplayReview()

print(review.review(session))