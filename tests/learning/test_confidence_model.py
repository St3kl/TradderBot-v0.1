from app.learning.confidence_model import ConfidenceModel

model = ConfidenceModel()

recommendation = {

    "confidence": 80

}

result = model.adjust(

    current_confidence=60,

    recommendation=recommendation

)

print()

print("Adjusted Confidence:", result)