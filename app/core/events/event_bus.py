from collections import defaultdict


class EventBus:

    def __init__(self):

        self._listeners = defaultdict(list)

    def subscribe(
        self,
        event_type,
        callback
    ):

        self._listeners[event_type].append(
            callback
        )

    def publish(self, event):

        event_type = type(event)

        listeners = self._listeners.get(
            event_type,
            []
        )

        for callback in listeners:

            callback(event)