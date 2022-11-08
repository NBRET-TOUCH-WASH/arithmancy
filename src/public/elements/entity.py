#coding:utf-8

#type hinting
from typing import List



#base class
from element import Element



#derived class
class Entity(Element):
    def __init__(self, name:str, tile:str, adjectives_list:List[str], hp:int, max_hp:int) -> None:
        super().__init__(name, tile)

        self.adjectives:List[str] = adjectives_list
        self.hp:int = hp
        self.max_hp:int = max_hp


    def move(self):
        raise NotImplementedError()

    def attack(self):
        raise NotImplementedError()