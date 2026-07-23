import time


class RetryEngine:

    def __init__(

        self,

        retries=3,

        delay=1

    ):

        self.retries = retries

        self.delay = delay

    def execute(

        self,

        function,

        *args,

        **kwargs

    ):

        last_error = None

        for attempt in range(

            1,

            self.retries + 1

        ):

            try:

                result = function(

                    *args,

                    **kwargs

                )

                return {

                    "success": True,

                    "attempt": attempt,

                    "result": result

                }

            except Exception as e:

                last_error = str(e)

                if attempt < self.retries:

                    time.sleep(self.delay)

                continue

        return {

            "success": False,

            "attempt": self.retries,

            "error": last_error

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("RETRY ENGINE")

        print("=" * 60)

        print()

        print("Success :", report["success"])

        print("Attempts:", report["attempt"])

        if report["success"]:

            print("Result  :", report["result"])

        else:

            print("Error   :", report["error"])