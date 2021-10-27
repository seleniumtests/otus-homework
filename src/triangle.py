from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    name = "triangle"

    def __new__(cls, first_side, second_side, third_side):
        if first_side > second_side + third_side or second_side > first_side + third_side or \
                third_side > first_side + second_side:
            return None
        else:
            instance = super(Triangle, cls).__new__(cls)
            instance.first_side, instance.second_side, instance.third_side = first_side, second_side, third_side
            return instance

    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    @property
    def area(self):
        half_perimeter = (self.first_side + self.second_side + self.third_side)/2
        return round(sqrt(half_perimeter*(half_perimeter - self.first_side)*(half_perimeter - self.second_side)
                    *(half_perimeter - self.third_side)), 2)

    @property
    def perimeter(self):
        return self.first_side + self.second_side + self.third_side


