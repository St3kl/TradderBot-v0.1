import os

from app.ai.providers.ollama_provider import OllamaProvider
from app.ai.providers.openrouter_provider import OpenRouterProvider
from app.ai.providers.groq_provider import GroqProvider
from app.ai.providers.openai_provider import OpenAIProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        provider = os.getenv(
            "AI_PROVIDER",
            "ollama"
        ).lower()

        if provider == "ollama":
            return OllamaProvider()

        if provider == "openrouter":
            return OpenRouterProvider()

        if provider == "groq":
            return GroqProvider()

        if provider == "openai":
            return OpenAIProvider()

        raise ValueError(
            f"Unknown AI provider: {provider}"
        )