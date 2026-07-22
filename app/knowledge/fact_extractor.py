class FactExtractor:
    """
    Extracts structured facts
    from completed trades.
    """

    def extract(self, trade):

        facts = []

        strategy = trade["strategy"]

        facts.append(

            (

                strategy,

                "market_regime",

                trade["market_regime"]

            )

        )

        facts.append(

            (

                strategy,

                "volatility",

                trade["volatility"]

            )

        )

        facts.append(

            (

                strategy,

                "session",

                trade["session_name"]

            )

        )

        facts.append(

            (

                strategy,

                "result",

                trade["result"]

            )

        )

        return facts