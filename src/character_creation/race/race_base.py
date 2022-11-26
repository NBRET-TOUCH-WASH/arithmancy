#coding:utf-8

#type hinting
from typing import List, Dict
from .racial_feat import RacialFeat, NoRacialFeat



#base class
class CharCreationRace:
    """Represents a race in the character creation segment. \
    Is not used in the main gameplay section.\n
    Serves as a base class for the other character creation segment races."""

    def __init__(self) -> None:
        self.name:str

        self.symbol:str
        self.info:str
        self.racial_feats:List[RacialFeat]

        self.artwork:str


    def __repr__(self) -> str:
        return f"{self.name} race"


    def handle_no_feats(self):
        if self.racial_feats == []:
            self.racial_feats = [NoRacialFeat()]


    #def get_number_of_artwork_lines(self):
    #    return len(self.artwork.splitlines())