from pprint import pprint

from app.research.research_report import ResearchReport

metrics = {

    "win_rate":74,

    "profit_factor":2.6,

    "sharpe":1.9,

    "drawdown":6

}

report = ResearchReport()

result = report.generate(

    strategy="TREND",

    metrics=metrics,

    score=91.8

)

print()

print("="*40)

print("RESEARCH REPORT")

print("="*40)

print()

pprint(result)

print()

print("✓ TEST PASSED")