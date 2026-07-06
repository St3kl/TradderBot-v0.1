from app.ai.providers.lmstudio_provider import LMStudioProvider

provider = LMStudioProvider()

response = provider.generate(
    "Say hello in one sentence."
)

print(response)