class EmergencyKillSwitch:

    def __init__(self):

        self.enabled = False
        self.reason = None

    def activate(self, reason):

        self.enabled = True
        self.reason = reason

    def deactivate(self):

        self.enabled = False
        self.reason = None

    def is_active(self):

        return self.enabled

    def get_reason(self):

        return self.reason

    def print(self):

        print()
        print("=" * 60)
        print("EMERGENCY KILL SWITCH")
        print("=" * 60)
        print()

        print("Active :", self.enabled)

        if self.reason:
            print("Reason :", self.reason)