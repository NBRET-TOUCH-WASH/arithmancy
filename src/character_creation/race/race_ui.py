#coding:utf-8

#type hinting
from typing import List
from tcod import Console

from .race_base import CharCreationRace



#modules
from assets import color_tokens
from .race_derived import *



#classes/instances
humankind = Human()
humankind2hominidBoogaloo = Human()
humankind3theApeWars = Human()
humankind4bananasOfTheApes = Human()
humankind5thePhantomApe = Human()

#the different races showed up on screen
available_races = [
    humankind,
    humankind2hominidBoogaloo,
    humankind3theApeWars,
    humankind4bananasOfTheApes,
    humankind5thePhantomApe
]



#variables
highlighted_row:int = 1

def clamp_highlighted_race(highlight:int, races:List[CharCreationRace]) -> None:
    """Clamps the race highlight in the range of the available races list.\n
    Returns nothing (`None`)."""
    if highlight < 1:
        return 1
    elif highlight > len(races):
        return len(races)
    else:
        return highlight



#functions
def print_races(console:Console, screen_width:int, screen_height:int, races:List[CharCreationRace], selected_row:int) -> None:
    """Prints the different available races to select as well as a small prompt.\n
    Returns nothing (`None`)."""

    printed_row = 1
    for r in range(len(available_races)):
        if printed_row == selected_row:
            console.print(3, 5+printed_row,
                        races[r].name,
                        color_tokens.WHITE.rgb,color_tokens.BLACK.rgb)
        else:
            console.print(3, 5+printed_row,
                        races[r].name,
                        color_tokens.CHARCOAL.rgb, color_tokens.BLACK.rgb)
        printed_row += 1


    console.print(3,3, "Select your character's fantasy race:", color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)



def print_info(console:Console, screen_width:int, screen_height:int):
    """Prints an info box-frame as well as a relatively short description of the highlighted race."""
    console.print_frame(screen_width-113,15, 35,37, "Info")