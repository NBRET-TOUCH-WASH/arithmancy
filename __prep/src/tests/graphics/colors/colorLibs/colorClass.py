#coding:utf-8

from typing import Tuple


#class ColorSet:
#    def __init__(self, *colors) -> None:
#        self.colorList = [colors]

class Color:
    def __init__(self, rgb:Tuple[int,int,int]) -> None:
        self.rgb = rgb
        self.hex = (hex(self.rgb[0]), hex(self.rgb[1]), hex(self.rgb[2]))

    def __repr__(self) -> str:
        return f"RGB: {self.rgb} | HEX: {self.hex}"

black = Color((0,0,0))
print(black)