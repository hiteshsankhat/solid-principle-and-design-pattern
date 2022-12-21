"""
Want to augment an object with additional functionality
Do not want to rewrite or alter existing code(OCP)
Want to keep new functionality separate(SRP)
Need to be able to interact with existing structures 
Two options:
    Inherit from required object(if possible)
    Build a decorator, which simply references the decorated objects

Define: Facilitates the addition of behaviors to individual objects without inheriting from them.

Summary:
    A decorator keeps the reference to the decorated objects
    Adds utility attributes and methods to augment the object's feature
    May or may not forward calls to the underlying object
    Proxy-ing of underlying calls can be done dynamically
    Python's functional decorators wrap functions; no direct relation to the GoF decorator pattern

"""
from abc import ABC
import time


def functionDecorator():
    def time_it(func):
        def wrapper():
            start = time.time()
            result = func()
            end = time.time()
            print(f"{func.__name__} took {int((end-start)*1000)}ms")

        return wrapper

    @time_it
    def some_op():
        print("Starting op")
        time.sleep(1)
        print("We are done")
        return 123

    if __name__ == "__main__":
        # some_op()
        # time_it(some_op)()
        some_op()


# functionDecorator()


def ClassicDecorator():
    class Shape(ABC):
        def __str__(self):
            return ""

    class Circle(Shape):
        def __init__(self, radius=0.0):
            self.radius = radius

        def resize(self, factor):
            self.radius *= factor

        def __str__(self):
            return f"A circle of radius {self.radius}"

    class Square(Shape):
        def __init__(self, side):
            self.side = side

        def __str__(self):
            return f"A square with side {self.side}"

    class ColoredShape(Shape):
        def __init__(self, shape, color):
            if isinstance(shape, ColoredShape):
                raise Exception("Cannot apply ColoredDecorator twice")
            self.shape = shape
            self.color = color

        def __str__(self):
            return f"{self.shape} has the color {self.color}"

    class TransparentShape(Shape):
        def __init__(self, shape, transparency):
            self.shape = shape
            self.transparency = transparency

        def __str__(self):
            return f"{self.shape} has {self.transparency * 100.0}% transparency"

    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape(circle, "red")
    print(red_circle)
    red_half_transparent_square = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_square)

    # mixed = ColoredShape(ColoredShape(Circle(3), "red"), "blue")
    # print(mixed)


# ClassicDecorator()
def DynamicDecorator():
    class FileWithLogging:
        def __init__(self, file):
            self.file = file

        def writelines(self, strings):
            self.file.writelines(strings)
            print(f"wrote {len(strings)} lines")

        def __iter__(self):
            return self.file.__iter__()

        def __next__(self):
            return self.file.__next__()

        def __getattr__(self, item):
            return getattr(self.__dict__["file"], item)

        def __setattr__(self, key, value):
            if key == "file":
                self.__dict__[key] = value
            else:
                setattr(self.__dict__["file"], key)

        def __delattr__(self, item):
            delattr(self.__dict__["file"], item)

    file = FileWithLogging(open("hello.txt", "w"))
    file.writelines(["hello", "world"])
    file.write("testing")
    file.close()


DynamicDecorator()
