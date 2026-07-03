from app.ai.prompt_builder import build_prompt
from app.ai.llm_client import ask_llm


def build_market_story(context):
    """
    Builds the AI narrative.
    """

    prompt = build_prompt(context)

    return ask_llm(prompt)