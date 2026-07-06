from pprint import pprint

from app.statistics.dashboard_engine import DashboardEngine


dashboard = DashboardEngine()

pprint(dashboard.build())