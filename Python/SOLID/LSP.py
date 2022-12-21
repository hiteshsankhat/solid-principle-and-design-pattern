class Rectangle:
    def __init__(self, height, width) -> None:
        self._height = height
        self._width = width

    @property
    def area(self):
        return self.width * self.height
    
    def __str__(self) -> str:
        return f'w: {self.width}, h: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'e: {expected}, g: {rc.area}')

rc = Rectangle(2, 3)
use_it(rc)