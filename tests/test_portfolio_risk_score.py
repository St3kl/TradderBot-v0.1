from app.portfolio.portfolio_risk_score import PortfolioRiskScore

engine = PortfolioRiskScore()

report = engine.calculate(

    concentration_ok=True,

    correlation_ok=False,

    heat_ok=True,

    drawdown_ok=True,

    diversification_score=90

)

engine.print(report)