from app.risk.exposure_manager import ExposureManager

manager = ExposureManager()

positions = []

print(manager.evaluate(positions))

positions = [{}] * 5

print(manager.evaluate(positions))