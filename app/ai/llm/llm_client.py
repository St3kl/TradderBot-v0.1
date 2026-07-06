import json
import requests

LM_STUDIO_URL = "http://127.0.0.1:12345/v1/chat/completions"

MODEL_NAME = "meta-llama-3.1-8b-instruct"



def ask_lmstudio(prompt: str):

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "You are an institutional trading analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 512,
        "stream": False
    }

    try:

        response = requests.post(
            LM_STUDIO_URL,
            json=payload,
            timeout=300
        )

        print(f"\nHTTP Status: {response.status_code}")

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException as e:
        raise RuntimeError(
            f"Unable to communicate with LM Studio:\n{e}"
        )

    except json.JSONDecodeError:
        raise RuntimeError(
            f"LM Studio returned invalid JSON:\n{response.text}"
        )

    # -----------------------------
    # Debug Output
    # -----------------------------

    print("\n========== LM STUDIO RESPONSE ==========")
    print(json.dumps(data, indent=4))

    # -----------------------------
    # Validate Response
    # -----------------------------

    if "choices" not in data:

        if "error" in data:
            raise RuntimeError(
                f"LM Studio Error:\n{json.dumps(data['error'], indent=4)}"
            )

        raise RuntimeError(
            f"Unexpected LM Studio response:\n{json.dumps(data, indent=4)}"
        )

    return data["choices"][0]["message"]["content"]

from app.ai.providers.provider_manager import ProviderManager


manager = ProviderManager()


def ask_llm(prompt):

    return manager.ask(prompt)