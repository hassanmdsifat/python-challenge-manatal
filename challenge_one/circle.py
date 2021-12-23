import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    circle_one = Circle(2.5)
    print(circle_one.calculate_area())
    print(circle_one.calculate_perimeter())