from pprint import pprint

from app.portfolio.group_exposure import GroupExposure

engine = GroupExposure()

pprint(engine.exposure())