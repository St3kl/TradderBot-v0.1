class EventDispatcher:

    def __init__(self):

        self.listeners = {}

    def subscribe(self, event, callback):

        self.listeners.setdefault(event, []).append(callback)

    def dispatch(self, event, data):

        for callback in self.listeners.get(event, []):

            callback(data)


dispatcher = EventDispatcher()