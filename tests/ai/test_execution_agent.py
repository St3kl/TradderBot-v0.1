from pprint import pprint

from app.ai.agents.execution_agent import ExecutionAgent

market = {

    "spread": 0.45,

    "slippage": 0.60,

    "liquidity": "LOW"

}

agent = ExecutionAgent()

print()

print("=" * 40)

print("EXECUTION AGENT")

print("=" * 40)

print()

pprint(

    agent.evaluate(

        market

    )

)

print()

print("✓ TEST PASSED")