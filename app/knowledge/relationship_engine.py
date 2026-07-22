from collections import defaultdict


class RelationshipEngine:
    """
    Learns relationship strengths between
    market facts.
    """

    def __init__(self):

        self.relationships = defaultdict(int)

    def update(self, facts):

        for subject, relation, obj in facts:

            key = (

                subject,

                relation,

                obj

            )

            self.relationships[key] += 1

    def get_strength(

        self,

        subject,

        relation,

        obj

    ):

        return self.relationships.get(

            (

                subject,

                relation,

                obj

            ),

            0

        )

    def summary(self):

        return dict(self.relationships)