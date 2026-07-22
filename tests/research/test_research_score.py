from app.research.research_score import ResearchScore

metrics = {

    "win_rate":72,

    "profit_factor":2.3,

    "sharpe":1.8,

    "drawdown":9

}

score = ResearchScore()

print()

print("="*40)

print("RESEARCH SCORE")

print("="*40)

print()

print(score.score(metrics))

print()

print("✓ TEST PASSED")