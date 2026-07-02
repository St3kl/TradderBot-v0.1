from app.confluence.engine import calculate_confluence


class ConfluenceStage:

    def run(self, session):

        print("Running Confluence Stage")

        session.confluence = calculate_confluence(
            bullish=session.bullish,
            pattern=session.pattern,
            structure=session.structure,
            volume=session.volume,
            alignment=session.alignment,
            smart_money=session.smart_money
        )

        return session