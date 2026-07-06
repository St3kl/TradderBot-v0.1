from app.config.ai_config import AI_PROVIDER

from app.ai.providers.lmstudio_provider import LMStudioProvider
from app.ai.providers.openai_provider import OpenAIProvider

# Future
# from app.ai.providers.ollama_provider import OllamaProvider


class ProviderManager:

    def __init__(self):

        if AI_PROVIDER == "lmstudio":

            self.provider = LMStudioProvider()

        elif AI_PROVIDER == "openai":

            self.provider = OpenAIProvider()

        # elif AI_PROVIDER == "ollama":
        #
        #     self.provider = OllamaProvider()

        else:

            raise RuntimeError(
                f"Unknown AI provider: {AI_PROVIDER}"
            )

    def ask(self, prompt):

        return self.provider.generate(prompt)