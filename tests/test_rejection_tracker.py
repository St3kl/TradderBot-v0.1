from app.history.rejection_tracker import RejectionTracker

tracker = RejectionTracker()

tracker.add([
    "Low Confidence",
    "Weak Volume"
])

tracker.add([
    "Low Confidence"
])

tracker.add([
    "Maximum exposure reached"
])

print(tracker.statistics())