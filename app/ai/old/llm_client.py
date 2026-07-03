from app.ai.providers.provider_factory import ProviderFactory


def ask_llm(prompt: str) -> str:
    """
    Uses the configured AI provider.
    """

    provider = ProviderFactory.get_provider()

    return provider.generate(prompt)