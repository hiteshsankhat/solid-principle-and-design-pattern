'''
Why we need this
    Object creation logic becomes too convoluted
    Initializer is not descriptive
        Name is always __init__
        Cannot overload with same sets of arguments with different name 
        Can turn into 'optional parameter hell
    Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to 
        A seperate method (Factory Method)
        That may exist in a separate class (Factory)
        Can create hierarchy of factories with Abstract Factory
Define: A component responsible solely for the wholesale creation of objects
'''
from abc import ABC
from enum import Enum
from math import *


def factoryMethodOrd():
    class CoordinateSystem(Enum):
        CARTESIAN = 1
        POLAR = 2

    class Point:
        ''' in python we can not overload init method '''

        def __init__(self, a, b, system=CoordinateSystem.CARTESIAN) -> None:
            if(system == CoordinateSystem.CARTESIAN):
                self.x = a
                self.y = b
            elif (system == CoordinateSystem.POLAR):
                self.x = a * cos(b)
                self.y = a * sin(b)

        def __str__(self) -> str:
            return f'x:{self.x} y: { self.y}'
    p = Point(1, 2, CoordinateSystem.CARTESIAN)
    p1 = Point(1, 2, CoordinateSystem.POLAR)
    print(p)
    print(p1)


def factoryMethod():
    class Point:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f'x:{self.x} y: { self.y}'

        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))
    p = Point(1, 2)
    p1 = Point.new_polar_point(1, 2)
    print(p)
    print(p1)


def factory():
    class Point:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f'x:{self.x} y: { self.y}'

        class PointFactory:
            def new_cartesian_point(self, x, y):
                return Point(x, y)

            def new_polar_point(self, rho, theta):
                return Point(rho * cos(theta), rho * sin(theta))
        factory = PointFactory()
    p = Point(1, 2)
    p1 = Point.factory.new_polar_point(1, 2)
    print(p)
    print(p1)


def abstractFactory():
    class HotDrink(ABC):
        def consume(self): pass

    class Tea(HotDrink):
        def consume(self):
            print("tea")

    class Coffee(HotDrink):
        def consume(self):
            print("Coffee")

    class HotDrinkFactory(ABC):
        def prepare(self, amount): pass

    class TeaFactory(HotDrinkFactory):
        def prepare(self, amount):
            print('tea', amount)
            return Tea()

    class CoffeeFactory(HotDrinkFactory):
        def prepare(self, amount):
            print('coffee', amount)
            return Coffee()

    drinks = {'tea': TeaFactory().prepare(200),
              'coffee': CoffeeFactory().prepare(100)}
    (drinks['coffee'].consume())
    (drinks['tea'].consume())

# factoryMethodOrd()
# factoryMethod()
# factory()

abstractFactory()