'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self, length, width):
        return self.length * self.width

    def rectangle_perimeter(self, length, width):
        return 2 * (self.length + self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_circumference(self, radius):
        return 2 * math.pi * self.radius

    def circle_area(self, radius):
        return self.radius / (2 * math.pi)




