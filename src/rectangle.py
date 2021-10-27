from src.figure import Figure


class Rectangle(Figure):
    name = "rectangle"

    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side

    @property
    def area(self):
        return self.first_side * self.second_side

    @property
    def perimeter(self):
        return 2*(self.first_side + self.second_side)