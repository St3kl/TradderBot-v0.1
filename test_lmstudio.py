import requests

url = "http://127.0.0.1:12345/v1/chat/completions"

payload = {
    "model": "meta-llama-3.1-8b-instruct",
    "messages": [
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ],
    "temperature": 0.1,
    "max_tokens": 20,
    "stream": False
}

response = requests.post(url, json=payload, timeout=300)

print(response.status_code)
print(response.text)


from app.ai.llm.lmstudio_client import ask_lmstudio

response = ask_lmstudio(
    "Say hello in one short sentence."
)

print("\n========== MODEL RESPONSE ==========\n")

print(response)