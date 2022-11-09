#coding:utf-8

#type hinting
from typing import List



#base class
class CharCreationRace:
    """Represents a race in the character creation segment. \
    Is not used in the main gameplay section.\n
    Serves as a base class for the other character creation segment races."""

    def __init__(self) -> None:
        self.name:str
        self.symbol:str
        self.info:str
        self.racial_feats:List[str]
        self.artwork:str