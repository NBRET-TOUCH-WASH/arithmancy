#coding:utf-8

from .rectangle import *

class Square(Rectangle):
    """Square class. Inherits from the `Rectangle` class.\n
    Allows to create and manipulate a square."""

    def __init__(self, sideLength):
        self.name = "Square"
        self.summits = 4

        #del self.width ; del self.length
        self.sideLength = sideLength
        self.width = self.sideLength
        self.length = self.sideLength

    def __repr__(self):
        return f"A {self.sideLength} unit(s)-sided square."

    def get_perimeter(self):
        return self.sideLength * 4

    def get_surface_area(self):
        return self.sideLength**2