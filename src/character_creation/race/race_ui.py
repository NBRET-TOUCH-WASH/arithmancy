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
    #? debug stuff
    #humankind2hominidBoogaloo = Human()
    #humankind3theApeWars = Human()
    #humankind4bananasOfTheApes = Human()
    #humankind5thePhantomApe = Human()

dwarvenkind = Dwarf()


#the different races showed up on screen
available_races = [
    humankind,
    dwarvenkind
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
def print_races(console:Console, screen_width:int, screen_height:int, races:List[CharCreationRace], highlighted_row:int) -> None:
    """Prints the different available races to select as well as a small prompt.\n
    Returns nothing (`None`)."""

    printed_row = 1
    for r in range(len(available_races)):
        if printed_row == highlighted_row:
            console.print(3, 5+printed_row,
                        races[r].name,
                        color_tokens.WHITE.rgb,color_tokens.BLACK.rgb)
        else:
            console.print(3, 5+printed_row,
                        races[r].name,
                        color_tokens.CHARCOAL.rgb, color_tokens.BLACK.rgb)
        printed_row += 1


    console.print(3,3, "Select your character's fantasy race:", color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)



def print_info(console:Console, screen_width:int, screen_height:int, races:List[CharCreationRace], highlighted_row:int):
    """Prints an info box-frame as well as a relatively short description of the highlighted race."""

    console.print_frame(screen_width-113,15,
                        35,37,
                        "Info")

    #console.print(screen_width-112,16,
    #            races[highlighted_row].info,
    #            color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
    console.print_rect(screen_width-111+31//2, (16+37)//2,
                        31,36,
                        races[highlighted_row-1].info,
                        alignment=2)



def print_feats(console:Console, screen_width:int, screen_height:int, races:List[CharCreationRace], highlighted_row:int):
    """Prints a symbol box-frame as well as the list of racial feats corresponding to the highlighted race."""

    console.print_frame(screen_width-76,15, 35,37, "Racial Feats")



def print_symbol(console:Console, screen_width:int, screen_height:int, races:List[CharCreationRace], highlighted_row:int):
    """Prints a symbol box-frame as well as the symbol corresponding to individuals of the highlighted race."""

    console.print_frame(screen_width-84,3, 15,10, "Race Symbol")
    console.print((screen_width-84+15//2) - len(races[highlighted_row-1].symbol)//2, 3+10//2,
                races[highlighted_row-1].symbol,
                color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)