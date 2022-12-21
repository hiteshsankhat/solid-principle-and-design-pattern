from enum import Enum
from typing import List


class Color(Enum):
    RED = 1,
    GREEN = 2,
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    name: str
    color: Color
    size: Size

    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products: List[Product], color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products: List[Product], size):
        for p in products:
            if p.color == size:
                yield p


class Specification:
    def is_satisfied(self, item) -> bool:
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, item) -> bool:
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]
    bf = BetterFilter()
    greenSpec = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, greenSpec):
        print(p.name)
    print("Large and Blue")
    large_blue = AndSpecification(
        SizeSpecification(Size.LARGE),
        ColorSpecification(Color.BLUE))
    l_B = SizeSpecification(Size.LARGE) & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(p.name)
    print("L and B")
    for p in bf.filter(products, l_B):
        print(p.name)