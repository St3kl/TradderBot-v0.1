from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found"
    )

client = OpenAI(
    api_key=api_key
)

def analyze_market(
    symbol,
    indicators,
    pattern
):

    prompt = f"""
    Symbol: {symbol}

    Price: {indicators['price']}

    RSI: {indicators['rsi']}

    EMA50: {indicators['ema50']}

    EMA200: {indicators['ema200']}

    Pattern:
    {pattern}

    Create:

    1. Market summary
    2. Bullish scenario
    3. Bearish scenario
    4. Confidence score
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content