import pytest

from src.square import Square
from src.circle import Circle
from src.rectangle import Rectangle
from src.triangle import Triangle


@pytest.fixture(scope='module')
def default_square():
    square = Square(square_side=7)
    yield square
    del square


@pytest.fixture(scope='module')
def default_circle():
    circle = Circle(radius=45)
    yield circle
    del circle


@pytest.fixture(scope='module')
def default_rectangle():
    rectangle = Rectangle(first_side=92, second_side=15)
    yield rectangle
    del rectangle


@pytest.fixture()
def default_triangle():
    triangle = Triangle(first_side=12, second_side=15, third_side=21)
    yield triangle
    del triangle


@pytest.fixture()
def triangle_with_bigger_first_side():
    triangle = Triangle(first_side=55, second_side=15, third_side=21)
    yield triangle
    del triangle


@pytest.fixture()
def triangle_with_bigger_second_side():
    triangle = Triangle(first_side=55, second_side=100, third_side=21)
    yield triangle
    del triangle


@pytest.fixture()
def triangle_with_bigger_third_side():
    triangle = Triangle(first_side=12, second_side=12, third_side=34)
    yield triangle
    del triangle
