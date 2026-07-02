from app.analysis.volume import analyze_volume


class VolumeStage:

    def run(self, session):

        print("Running Volume Stage")

        if "volumes" in session.indicators:

            session.volume = analyze_volume(
                session.indicators["volumes"]
            )

        else:

            session.volume = {
                "strength": "N/A",
                "score": 10
            }

        return session