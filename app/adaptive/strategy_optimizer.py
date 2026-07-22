class StrategyOptimizer:

    def optimize(self, learning_stats):

        recommendations = []

        for strategy, stats in learning_stats.items():

            winrate = stats.get("win_rate", 0)
            total = stats.get("total", 0)

            if total < 10:
                recommendations.append({
                    "strategy": strategy,
                    "action": "Collect More Data"
                })

            elif winrate < 40:
                recommendations.append({
                    "strategy": strategy,
                    "action": "Disable"
                })

            elif winrate < 55:
                recommendations.append({
                    "strategy": strategy,
                    "action": "Review Rules"
                })

            elif winrate < 70:
                recommendations.append({
                    "strategy": strategy,
                    "action": "Keep"
                })

            else:
                recommendations.append({
                    "strategy": strategy,
                    "action": "Increase Priority"
                })

        return recommendations

    def print(self, recommendations):

        print()
        print("=" * 60)
        print("STRATEGY OPTIMIZER")
        print("=" * 60)

        for rec in recommendations:

            print(
                f"{rec['strategy']:<15} -> {rec['action']}"
            )