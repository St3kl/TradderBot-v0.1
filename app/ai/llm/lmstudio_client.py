import json
import requests

LM_STUDIO_URL = "http://127.0.0.1:12345/v1/chat/completions"


def ask_lmstudio(prompt):

    payload = {
        "model": "meta-llama-3.1-8b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 512,
        "stream": False
    }

    response = requests.post(
        LM_STUDIO_URL,
        json=payload,
        timeout=300
    )

    print("\nSTATUS:", response.status_code)

    data = response.json()

    print("\nFULL RESPONSE:")
    print(json.dumps(data, indent=2))

    if "choices" not in data:
        raise Exception("LM Studio returned an unexpected response.")

    return data["choices"][0]["message"]["content"]