from app.ai.providers.base_provider import BaseProvider


class OpenRouterProvider(BaseProvider):

    def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "OpenRouter provider not implemented yet."
        )