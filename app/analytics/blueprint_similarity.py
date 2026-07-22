class BlueprintSimilarity:

    def compare(self, blueprint, trade):

        score = 0
        total = 0

        # Strategy
        total += 1
        if trade.get("strategy") == blueprint.get("ideal_strategy"):
            score += 1

        # Market Regime
        total += 1
        if trade.get("market_regime") == blueprint.get("ideal_market"):
            score += 1

        # Signals
        ideal = set(blueprint.get("ideal_signals", []))
        current = set(trade.get("signals", []))

        total += len(ideal)

        score += len(ideal.intersection(current))

        similarity = round(score / total * 100, 2)

        return {

            "similarity": similarity,

            "matches": list(

                ideal.intersection(current)

            ),

            "missing": list(

                ideal.difference(current)

            )

        }

    def print(self, result):

        print()

        print("=" * 60)

        print("BLUEPRINT SIMILARITY")

        print("=" * 60)

        print()

        print("Similarity :", result["similarity"], "%")

        print()

        print("Matched")

        for item in result["matches"]:

            print("-", item)

        print()

        print("Missing")

        for item in result["missing"]:

            print("-", item)