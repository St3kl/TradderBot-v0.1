from app.ai.providers.provider_manager import ProviderManager

provider = ProviderManager()

response = provider.ask("Hello")

print(response)