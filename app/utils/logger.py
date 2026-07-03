from datetime import datetime


def log(message):

    log(
        f"[{datetime.now().strftime('%H:%M:%S')}] {message}"
    )