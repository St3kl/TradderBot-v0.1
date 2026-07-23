from datetime import datetime


class ExecutionMonitor:

    def inspect(self, orders):

        report = {

            "pending": [],

            "partial": [],

            "filled": [],

            "cancelled": [],

            "rejected": []

        }

        for order in orders:

            status = order.get("status", "")

            if status == "PENDING":
                report["pending"].append(order)

            elif status == "PARTIAL":
                report["partial"].append(order)

            elif status == "FILLED":
                report["filled"].append(order)

            elif status == "CANCELLED":
                report["cancelled"].append(order)

            elif status == "REJECTED":
                report["rejected"].append(order)

        report["timestamp"] = datetime.utcnow()

        return report

    def print(self, report):

        print()

        print("=" * 60)
        print("EXECUTION MONITOR")
        print("=" * 60)
        print()

        print("Pending   :", len(report["pending"]))
        print("Partial   :", len(report["partial"]))
        print("Filled    :", len(report["filled"]))
        print("Cancelled :", len(report["cancelled"]))
        print("Rejected  :", len(report["rejected"]))