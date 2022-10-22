#coding:utf-8

class Shape:
    """Shape class.\n
    Allows to create a geometrical shape."""

    def __init__(self, name:str, summits:int):
        self.name = name
        self.summits = summits

    def __repr__(self):
        return f"A {self.summits}-summits geometrical shape. Colloquially known as a(n) \"{self.name}\"."