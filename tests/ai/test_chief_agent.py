from pprint import pprint

from app.ai.agents.chief_agent import ChiefAgent

chief = ChiefAgent()

reports = [

    {

        "agent":"Bull",

        "score":90,

        "reasons":[

            "Strong trend"

        ]

    },

    {

        "agent":"Bear",

        "score":20,

        "reasons":[

            "Minor resistance"

        ]

    },

    {

        "agent":"Risk",

        "score":95,

        "reasons":[

            "Low drawdown"

        ]

    },

    {

        "agent":"Execution",

        "score":100,

        "reasons":[

            "Excellent liquidity"

        ]

    },

    {

        "agent":"Research",

        "score":100,

        "reasons":[

            "Excellent research"

        ]

    }

]

decision = chief.decide(

    reports

)

print()

print("=" * 40)

print("CHIEF AGENT")

print("=" * 40)

print()

pprint(decision)

print()

print("✓ TEST PASSED")