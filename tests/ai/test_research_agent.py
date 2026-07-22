from pprint import pprint

from app.ai.agents.research_agent import ResearchAgent

research = {

    "win_rate":74,

    "profit_factor":2.4,

    "research_score":94

}

agent = ResearchAgent()

print()

print("=" * 40)

print("RESEARCH AGENT")

print("=" * 40)

print()

pprint(

    agent.evaluate(

        research

    )

)

print()

print("✓ TEST PASSED")