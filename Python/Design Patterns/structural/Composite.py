"""
Objects use other objects properties/members through inheritance and composition
Composition lets us make compound objects
    E.g. a mathematical expression composed of simple expressions; or 
    A grouping of shapes that consists of several shapes 
Composite design pattern is used to treat both single and composite objects uniformly
    i.e., Foo and sequence (yielding Foo's) have common APIs

Define: A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.

Summary: 
    Objects can use other objects via inheritance/composition
    Some composed and singular objects need similar/identical behaviors 
    Composite design pattern lets us treat both types of objects uniformly
    Python supports iteration with __iter__ the Iterable ABC
    A single object can make itself iterable by yielding self from __iter__
"""


from abc import ABC
from collections.abc import Iterable


def GeoMetricShapes():
    class GraphicObject:
        def __init__(self, color=None) -> None:
            self.color = color
            self.children = []
            self._name = "Group"

        @property
        def name(self):
            return self._name

        def _print(self, items, depth):
            items.append("*" * depth)
            if self.color:
                items.append(self.color)
            items.append(f"{self.name}\n")
            for child in self.children:
                child._print(items, depth + 1)

        def __str__(self):
            items = []
            self._print(items, 0)
            return "".join(items)

    class Circle(GraphicObject):
        @property
        def name(self):
            return "Circle"

    class Square(GraphicObject):
        @property
        def name(self):
            return "Square"

    drawing = GraphicObject()
    drawing._name = "My Drawing"
    drawing.children.append(Square("Red"))
    drawing.children.append(Circle("Yellow"))

    group = GraphicObject()  # no name
    group.children.append(Circle("Blue"))
    group.children.append(Square("Blue"))
    drawing.children.append(group)

    print(drawing)


# GeoMetricShapes()


def NeuralNetworks():
    class Connectable(Iterable, ABC):
        def connect_to(self, other):
            if self == other:
                return

            for s in self:
                for o in other:
                    s.outputs.append(o)
                    o.inputs.append(s)

    class Neuron(Connectable):
        def __init__(self, name):
            self.name = name
            self.inputs = []
            self.outputs = []

        def __str__(self):
            return (
                f"{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs"
            )

        def __iter__(self):
            yield self

    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)

    class NeuronLayer(list, Connectable):
        def __init__(self, name, count):
            super().__init__()
            self.name = name
            for x in range(0, count):
                self.append(Neuron(f"{name}-{x}"))

        def __str__(self):
            return f"{self.name} with {len(self)} neurons"

    neuron1 = Neuron("n1")
    neuron2 = Neuron("n2")
    layer1 = NeuronLayer("L1", 3)
    layer2 = NeuronLayer("L2", 4)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)
NeuralNetworks()