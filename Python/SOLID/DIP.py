from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class person:
    def __init__(self, name) -> None:
        self.name = name

class Relationships:
    def __init__(self) -> None:
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.CHILD, child))
        self.relations.append(
            (child, Relationship.PARENT, parent))

class Research:
    def __init__(self, relationships) -> None:
        relations = relationships.relations
        for r in relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print('Found')