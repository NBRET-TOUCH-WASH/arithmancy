#coding:utf-8

from typing import Tuple

class Entity:
    """A class used to represent a game object."""

    def __init__(self, x:int, y:int, char:str, color:Tuple[int, int, int]) -> None:
        self.x = x
        self.y = y

        self.char = char
        self.color = color


    def move(self, dx:int, dy:int) -> None:
        """Moves the entity by a specified number of tiles.\n
        Returns nothing (`None`)."""

        self.x += dx
        self.y += dy