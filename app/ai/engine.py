from app.ai.context.context_builder import build_ai_context
from app.ai.reasoning.reasoning_engine import build_reasoning
from app.ai.prompts.prompt_builder import build_prompt
from app.ai.llm.llm_client import ask_llm
from app.ai.parser.response_parser import parse_response


class AIEngine:
    """
    AI Processing Pipeline

    TradingSession
        ↓
    Context Builder
        ↓
    Reasoning Engine
        ↓
    Prompt Builder
        ↓
    LLM
        ↓
    Parser
        ↓
    AI Report
    """

    def analyze(self, session):

        # -----------------------------
        # Build Context
        # -----------------------------
        context = build_ai_context(session)

        # -----------------------------
        # Build Reasoning
        # -----------------------------
        context["reasoning"] = build_reasoning(context)

        # -----------------------------
        # Build Prompt
        # -----------------------------
        prompt = build_prompt(context)

        # -----------------------------
        # Ask LLM
        # -----------------------------
        response = ask_llm(prompt)

        # -----------------------------
        # Parse Response
        # -----------------------------
        report = parse_response(response)

        return report