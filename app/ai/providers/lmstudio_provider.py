from app.ai.providers.provider import AIProvider
from app.ai.llm.lmstudio_client import ask_lmstudio


class LMStudioProvider(AIProvider):

    def generate(self, prompt):

        return ask_lmstudio(prompt)