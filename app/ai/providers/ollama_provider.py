from app.ai.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "Ollama provider not implemented yet."
        )