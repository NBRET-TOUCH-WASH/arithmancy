#coding:utf-8

from .shape import *

class Rectangle(Shape):
    """Rectangle class. Inherits from the `Shape` class.\n
    Allows to create and manipulate a rectangle."""

    def __init__(self, width, length):
        self.name = "Rectangle"

        self.summits = 4
        #del self.summits

        self.width = width
        self.length = length

    def get_perimeter(self):
        return self.width*2 + self.length*2

    def get_surface_area(self):
        return self.width * self.length

    def __repr__(self):
        return f"A {self.width}x{self.length} rectangle."