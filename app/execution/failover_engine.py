class FailoverEngine:

    def __init__(self):

        self.primary = None

        self.backups = []

    def configure(

        self,

        primary,

        backups

    ):

        self.primary = primary

        self.backups = backups

    def get_available(self):

        if self.primary.is_connected():

            return self.primary

        for broker in self.backups:

            if broker.is_connected():

                return broker

        return None

    def print(self):

        print()

        print("=" * 60)

        print("FAILOVER STATUS")

        print("=" * 60)

        print()

        if self.primary:

            print("Primary Connected :", self.primary.is_connected())

        print()

        for i, broker in enumerate(self.backups, start=1):

            print(

                f"Backup {i} Connected :",

                broker.is_connected()

            )