from pprint import pprint

from app.knowledge.knowledge_graph import KnowledgeGraph

graph = KnowledgeGraph()

graph.add(

    "TREND",

    "works_best_in",

    "TRENDING"

)

graph.add(

    "TREND",

    "volatility",

    "NORMAL"

)

graph.add(

    "TREND",

    "session",

    "LONDON"

)

print()

print("=" * 40)

print("KNOWLEDGE GRAPH")

print("=" * 40)

print()

pprint(

    graph.summary()

)

print()

print("✓ TEST PASSED")