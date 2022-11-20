#coding:utf-8

#type hinting
from typing import Dict, List, Tuple

from assets import color_tokens



#base class
class CharCreationClass:
    """Represents a class in the character creation segment. \
    Is not used in the main gameplay section.\n
    Serves as a base class for the other character creation segment classes."""

    mod_types:Dict[str:color_tokens.Color, str:color_tokens.Color] = {
        "BUFF":color_tokens.GREEN,
        "NEUTRAL":color_tokens.CHARCOAL,
        "DEBUFF":color_tokens.RED
    }

    def __init__(self) -> None:
        self.name:str

        self.color:Tuple[int, int, int]
        self.info:str
        self.attributes_modifiers:List[Tuple[str,str,str]]

        self.artwork:str


    def __repr__(self) -> str:
        return f"{self.name} class"


    #def get_number_of_artwork_lines(self):
    #    return len(self.artwork.splitlines())