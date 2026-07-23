from app.execution.retry_engine import RetryEngine

engine = RetryEngine(

    retries=3,

    delay=0

)

counter = {

    "value": 0

}


def unstable():

    counter["value"] += 1

    if counter["value"] < 3:

        raise Exception("Temporary Failure")

    return "Order Submitted"


report = engine.execute(unstable)

engine.print(report)