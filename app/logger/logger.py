import logging


class Logger:

    @staticmethod
    def get(name="TradderBot"):

        logging.basicConfig(

            level=logging.INFO,

            format=(
                "%(asctime)s | "
                "%(levelname)-8s | "
                "%(name)s | "
                "%(message)s"

            )

        )

        return logging.getLogger(name)