class VolumeEngine:
    """
    Evaluates market participation.

    Responsible for interpreting:

    - Relative volume
    - Volume spikes
    - Buying pressure
    - Selling pressure
    - Volume strength
    """

    def analyze(self, session):

        volume = session.volume

        strength = volume.get("strength", 0)

        status = volume.get("status", "Unknown")

        return {

            "status": status,

            "strength": strength

        }