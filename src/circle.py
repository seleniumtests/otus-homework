from src.figure import Figure


class Circle(Figure):
    name = "circle"

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.Pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * self.Pi * self.radius
