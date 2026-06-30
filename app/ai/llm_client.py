import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_llm(prompt):
    """
    Sends the prompt to the LLM and
    returns the generated response.
    """

    try:

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an institutional trader with expertise in "
                        "ICT, Smart Money Concepts, Wyckoff, order flow, "
                        "market structure, and risk management."
                    )
                },

                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,

            max_tokens=400
        )

        return response.choices[0].message.content

    except Exception as e:

        print("LLM ERROR:", e)

        return (
            "AI analysis is temporarily unavailable."
        )