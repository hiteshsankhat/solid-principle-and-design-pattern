"""
Bridge prevents a Cartesian product complexity explosion
Example:
    Base class ThreadScheduler 
    Can be preemptive or cooperative
    Can run on window or Unix
    End up with a 2x2 scenario: WindowsPTS, UnixPTS, WindowsCTS, UnixCTS
Bridge pattern avoids the entity explosion

Define: A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy)
"""
# Circles and squares
# Each can be rendered in vector or raster form


class Renderer:
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for circle of radius {radius}")


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
