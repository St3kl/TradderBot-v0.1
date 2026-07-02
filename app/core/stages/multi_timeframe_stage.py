from app.analysis.multi_timeframe import (
    analyze_timeframes,
    calculate_alignment
)


class MultiTimeframeStage:

    def run(self, session):

        print("Running Multi-Timeframe Stage")

        if session.symbol.endswith("USDT"):

            session.mtf = analyze_timeframes(
                session.symbol
            )

            session.alignment = calculate_alignment(
                session.mtf
            )

            report = ""

            for tf, info in session.mtf.items():

                trend = (
                    "Bullish"
                    if info["bullish"]
                    else "Bearish"
                )

                report += f"{tf}: {trend}\n"

            session.tf_report = report

        else:

            session.mtf = None
            session.alignment = 0
            session.tf_report = "Forex MTF Coming Soon\n"

        return session