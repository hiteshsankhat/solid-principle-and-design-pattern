"""
Electrical devices have different power (interface) requirements
    Voltage (5V, 220V)
    Socket/ plug type
We cannot modify our gadgets to support every possible interface 
    Some support possible
Thus, we use a special device to give us the interface we require from the interface we have

Define: A construct which adapts an existing interface X to conform to the required interface Y.
"""


def adapter_no_cache():
    class Point:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y

    def draw_point(p):
        print(".", end="")

    class Line:
        def __init__(self, start, end) -> None:
            self.start = start
            self.end = end

    class Rectangle(list):
        """Represented as a list of lines."""

        def __init__(self, x, y, width, height):
            super().__init__()
            self.append(Line(Point(x, y), Point(x + width, y)))
            self.append(Line(Point(x + width, y), Point(x + width, y + height)))
            self.append(Line(Point(x, y), Point(x, y + height)))
            self.append(Line(Point(x, y + height), Point(x + width, y + height)))

    class LineToPointAdapter(list):
        count = 0

        def __init__(self, line):
            self.count += 1
            print(
                f"{self.count}: Generating points for line "
                f"[{line.start.x},{line.start.y}]→"
                f"[{line.end.x},{line.end.y}]"
            )

            left = min(line.start.x, line.end.x)
            right = max(line.start.x, line.end.x)
            top = min(line.start.y, line.end.y)
            bottom = min(line.start.y, line.end.y)

            if right - left == 0:
                for y in range(top, bottom):
                    self.append(Point(left, y))
            elif line.end.y - line.start.y == 0:
                for x in range(left, right):
                    self.append(Point(x, top))

    def draw(rcs):
        print("\n\n--- Drawing some stuff ---\n")
        for rc in rcs:
            for line in rc:
                adapter = LineToPointAdapter(line)
                for p in adapter:
                    draw_point(p)

    rs = [Rectangle(1, 1, 10, 10), Rectangle(3, 3, 6, 6)]
    draw(rs)
    draw(rs)


adapter_no_cache()


def adapter_with_cache():
    class Point:
        def __init__(self, x, y):
            self.y = y
            self.x = x

    def draw_point(p):
        print(".", end="")

    # ^^ you are given this

    # vv you are working with this

    class Line:
        def __init__(self, start, end):
            self.end = end
            self.start = start

    class Rectangle(list):
        """Represented as a list of lines."""

        def __init__(self, x, y, width, height):
            super().__init__()
            self.append(Line(Point(x, y), Point(x + width, y)))
            self.append(Line(Point(x + width, y), Point(x + width, y + height)))
            self.append(Line(Point(x, y), Point(x, y + height)))
            self.append(Line(Point(x, y + height), Point(x + width, y + height)))

    class LineToPointAdapter:
        count = 0
        cache = {}

        def __init__(self, line):
            self.h = hash(line)
            if self.h in self.cache:
                return

            super().__init__()
            self.count += 1
            print(
                f"{self.count}: Generating points for line "
                + f"[{line.start.x},{line.start.y}]→[{line.end.x},{line.end.y}]"
            )

            left = min(line.start.x, line.end.x)
            right = max(line.start.x, line.end.x)
            top = min(line.start.y, line.end.y)
            bottom = min(line.start.y, line.end.y)

            points = []

            if right - left == 0:
                for y in range(top, bottom):
                    points.append(Point(left, y))
            elif line.end.y - line.start.y == 0:
                for x in range(left, right):
                    points.append(Point(x, top))

            self.cache[self.h] = points

        def __iter__(self):
            return iter(self.cache[self.h])

    def draw(rcs):
        print("Drawing some rectangles...")
        for rc in rcs:
            for line in rc:
                adapter = LineToPointAdapter(line)
                for p in adapter:
                    draw_point(p)
        print("\n")

    rs = [Rectangle(1, 1, 10, 10), Rectangle(3, 3, 6, 6)]

    draw(rs)
    draw(rs)

    # can define your own hashes or use the defaults
    print(hash(Line(Point(1, 1), Point(10, 10))))
