import os
import requests

from app.ai.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def __init__(self):

        self.url = "http://localhost:11434/api/generate"

        self.model = os.getenv(
            "OLLAMA_MODEL",
            "qwen3:8b"
        )

    def generate(self, prompt: str) -> str:

        payload = {

            "model": self.model,

            "prompt": prompt,

            "stream": False

        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            return data["response"]

        except Exception as e:

            print("OLLAMA ERROR:", e)

            return (
                "AI analysis unavailable."
            )