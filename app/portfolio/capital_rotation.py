class CapitalRotation:

    def allocate(self, strategies, capital):

        total_score = sum(

            max(s["score"], 0)

            for s in strategies

        )

        allocation = []

        if total_score == 0:

            return allocation

        for strategy in strategies:

            percent = strategy["score"] / total_score

            allocation.append({

                "strategy": strategy["name"],

                "score": strategy["score"],

                "allocation_percent": round(percent * 100, 2),

                "capital": round(capital * percent, 2)

            })

        allocation.sort(

            key=lambda x: x["capital"],

            reverse=True

        )

        return allocation

    def print(self, allocation):

        print()

        print("=" * 60)

        print("CAPITAL ROTATION")

        print("=" * 60)

        print()

        for row in allocation:

            print(

                f"{row['strategy']:<12}"

                f"{row['allocation_percent']:>7}%"

                f"   ${row['capital']:.2f}"

            )