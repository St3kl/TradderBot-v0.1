from collections import defaultdict


class KnowledgeGraph:
    """
    Stores relationships discovered
    from completed trades.
    """

    def __init__(self):

        self.graph = defaultdict(list)

    def add(

        self,

        subject,

        relation,

        obj

    ):

        self.graph[subject].append(

            {

                "relation": relation,

                "object": obj

            }

        )

    def get(

        self,

        subject

    ):

        return self.graph.get(

            subject,

            []

        )

    def summary(self):

        return dict(self.graph)