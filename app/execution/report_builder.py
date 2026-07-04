def build_execution_report(execution):

    risk = execution["risk"]

    exposure = risk["exposure"]

    portfolio = risk["portfolio"]

    position = risk["position"]

    confirmation = execution["confirmation"]

    report = {

        "status": (
            "READY TO EXECUTE"
            if execution["execute"]
            else "WAIT"
        ),

        "position_size": position["position_size"],

        "risk_amount": position["risk_amount"],

        "stop_distance": position["stop_distance"],

        "portfolio_risk": portfolio["total_risk"],

        "open_positions": portfolio["positions"],

        "long_exposure": exposure["long_risk"],

        "short_exposure": exposure["short_risk"],

        "net_exposure": exposure["net_exposure"],

        "confirmation_score": confirmation["score"],

        "confirmations": confirmation["confirmations"],

        "approved": risk["approved"],

        "warnings": risk["reasons"]

    }

    return report