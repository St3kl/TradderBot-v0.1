class SafeStage:
    """
    Base class for every pipeline stage.

    Guarantees:

    • Never crashes the pipeline.
    • Produces defaults when needed.
    • Logs failures.
    """

    name = "Unnamed Stage"

    def run(self, session):

        try:

            return self.execute(session)

        except Exception as e:

            print()

            print("=" * 60)
            print(f"{self.name} FAILED")
            print("=" * 60)

            print(e)

            if not hasattr(session, "errors"):

                session.errors = []

            session.errors.append({

                "stage": self.name,

                "error": str(e)

            })

            return session

    def execute(self, session):

        raise NotImplementedError()