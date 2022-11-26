#coding:utf-8

class Element:
    """Game element class.\n
    Serves as the highest base class for all custom game elements."""

    def __init__(self, name:str, tile:str) -> None:
        self.name:str = name
        self.tile:str = tile

    def __repr__(self) -> str:
        return f"{self.tile} : {self.name}"