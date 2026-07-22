
#move to ai

class ConfidenceModel:
    """
    Adjusts confidence based on historical performance.
    """

    def adjust(
        self,
        current_confidence,
        recommendation
    ):

        confidence = current_confidence

        historical = recommendation["confidence"]

        # Blend both confidences
        confidence = int(

            (confidence * 0.7) +

            (historical * 0.3)

        )

        confidence = max(0, min(confidence, 100))

        return confidence