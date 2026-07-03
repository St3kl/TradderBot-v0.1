import os

# LM Studio Configuration
LM_STUDIO_HOST = os.getenv("LM_STUDIO_HOST", "127.0.0.1")
LM_STUDIO_PORT = int(os.getenv("LM_STUDIO_PORT", "12345"))

LM_STUDIO_URL = (
    f"http://{LM_STUDIO_HOST}:{LM_STUDIO_PORT}/v1/chat/completions"
)

MODEL_NAME = os.getenv(
    "LM_STUDIO_MODEL",
    "meta-llama-3.1-8b-instruct"
)

TEMPERATURE = 0.2
MAX_TOKENS = 700
TIMEOUT = 300