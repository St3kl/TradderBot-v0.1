class BrokerFactory:

    @staticmethod
    def create(name):

        if name == "paper":

            from app.paper.paper_broker import PaperBroker

            return PaperBroker()

        raise ValueError(

            f"Unknown broker: {name}"

        )