from app.ai.providers.provider_manager import ProviderManager


class AIHealth:

    def __init__(self):

        self.provider = ProviderManager()

    def check(self):

        try:

            self.provider.ask("Reply only with: OK")

            return True

        except Exception:

            return False