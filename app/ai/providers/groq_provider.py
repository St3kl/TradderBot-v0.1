from app.ai.providers.base_provider import BaseProvider


class GroqProvider(BaseProvider):

    def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "Groq provider not implemented yet."
        )