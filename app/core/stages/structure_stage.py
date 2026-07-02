from app.market_structure.structure import analyze_structure


class StructureStage:

    def run(self, session):

        print("Running Structure Stage")

        session.structure = analyze_structure(
            highs=session.indicators["highs"],
            lows=session.indicators["lows"],
            closes=session.indicators["closes"],
            bullish=session.bullish
        )

        return session