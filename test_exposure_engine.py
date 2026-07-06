from pprint import pprint

from app.portfolio.exposure_engine import ExposureEngine

engine = ExposureEngine()

pprint(engine.current_exposure())