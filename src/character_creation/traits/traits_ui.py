#coding:utf-8

#type hinting
from typing import List, Dict
from tcod import Console
from tcod.constants import *




#modules
from public.data.data import player_mods
from assets import color_tokens



#classes/instances
class Attribute:
    """Represents a character attribute during the character creation segment."""
    def __init__(self) -> None:
        self.symbol:str = "SYM"
        self.value:int = 0
        self.description:str = "SAMPLE_TXT"

class Constitution(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.symbol = "CON"
        self.description = "The character's ability to resist and recover from damage received."

class Dexterity(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.symbol = "DEX"
        self.description = "Combination of the character's agility and quickness."

class Intelligence(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.symbol = "INT"
        self.description = "Spellcasting abilities of spellcasters from the arcane and shadow realms."

class Strength(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.symbol = "STR"
        self.description = "Character's aw physical strength."

class Wisdom(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.symbol = "WIS"
        self.description = "Ability of a cleric to use prayers, verses, just like intelligence affects spellcasting."

con_attrib = Constitution()
dex_attrib = Dexterity()
int_attrib = Intelligence()
str_attrib = Strength()
wis_attrib = Wisdom()
listed_attributes:List[Attribute] = [
    con_attrib,
    dex_attrib,
    int_attrib,
    str_attrib,
    wis_attrib
]



#variables
highlighted_row:int = 1

def clamp_highlighted_attrib(attrib_highlight:int, attrib_list:List[Attribute]) -> None:
    """Clamps the attribute highlight in the range of the attributes list.\n
    Returns nothing (`None`)."""
    if attrib_highlight < 1:
        return 1
    elif attrib_highlight > len(attrib_list):
        return len(attrib_list)
    else:
        return attrib_highlight



#functions
def print_attributes(console:Console, screen_width:int, screen_height:int, attrib_list:List[Attribute], highlighted_row:int, player_mods:List[int]) -> None:
    """Prints the different available races to select as well as a small prompt.\n
    Returns nothing (`None`)."""

    screen_third:int = screen_width//3

    printed_row = 1
    for a in range(len(listed_attributes)):
        ATTRIB_IS_BUFF = attrib_list[a].value > 0
        ATTRIB_IS_NEUTRAL = attrib_list[a].value == 0

        MOD_IS_BUFF = player_mods[a] > 0
        MOD_IS_NEUTRAL = player_mods[a] == 0
        MOD_IS_DEBUFF = player_mods[a] < 0

        if printed_row == highlighted_row:
            console.print(screen_third, 10+printed_row,
                        attrib_list[a].symbol,
                        color_tokens.WHITE.rgb,color_tokens.BLACK.rgb)
            console.print(screen_width//2, 10+printed_row,
                        "=",
                        color_tokens.WHITE.rgb, color_tokens.BLACK.rgb,
                        alignment=CENTER)
            if ATTRIB_IS_BUFF:
                console.print(screen_third*2, 10+printed_row, "+{}".format(str(attrib_list[a].value)), color_tokens.GREEN.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            elif ATTRIB_IS_NEUTRAL:
                console.print(screen_third*2, 10+printed_row, str(attrib_list[a].value), color_tokens.ASH.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            #elif ATTRIB_IS_DEBUFF:
            #    console.print(screen_third*2, 10+printed_row, str(attrib_list[a].value), color_tokens.RED.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)

        else:
            console.print(screen_third, 10+printed_row,
                        attrib_list[a].symbol,
                        color_tokens.CHARCOAL.rgb, color_tokens.BLACK.rgb)
            console.print(screen_width//2,10+printed_row, "=", color_tokens.CHARCOAL.rgb, color_tokens.BLACK.rgb, alignment=CENTER)
            if ATTRIB_IS_BUFF:
                console.print(screen_third*2, 10+printed_row, "+{}".format(str(attrib_list[a].value)), color_tokens.DARK_GREEN.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            elif ATTRIB_IS_NEUTRAL:
                console.print(screen_third*2, 10+printed_row, str(attrib_list[a].value), color_tokens.TAUPE.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            #elif ATTRIB_IS_DEBUFF:
            #    console.print(screen_third*2, 10+printed_row, str(attrib_list[a].value), color_tokens.MAROON.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
        printed_row += 1


    console.print(3,3, "Tweak your character's attributes to your liking:", color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
    console.print(screen_width//2,screen_height-7, "Press the [UP] and [DOWN] arrow keys to raise or lower the attribute highlight.", color_tokens.FERN_GREEN.rgb, color_tokens.BLACK.rgb, alignment=CENTER)
    console.print(screen_width//2,screen_height-6, "Press the [+] and [-] keys on your keypad to increment or decrement the highlighted attribute.", color_tokens.FERN_GREEN.rgb, color_tokens.BLACK.rgb, alignment=CENTER)
    console.print(screen_width//2,screen_height-4, "Press [ENTER] to submit your choices and finish character creation.", color_tokens.FERN_GREEN.rgb, color_tokens.BLACK.rgb, alignment=CENTER)



def print_info(console:Console, screen_width:int, screen_height:int, attrib_list:List[Attribute], highlighted_row:int):
    """Prints an info box-frame as well as a relatively short description of the highlighted race."""

    console.print_frame(screen_width-113,15,
                        35,37,
                        "Info")

    #console.print(screen_width-112,16,
    #            races[highlighted_row].info,
    #            color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
    console.print_rect(screen_width-111+31//2, 17,
                        31,36,
                        classes[highlighted_row-1].info,
                        alignment=2)



def print_artwork(console:Console, screen_width:int, screen_height:int, attrib_list:List[Attribute], highlighted_row:int):
    """Prints an artwork box-frame as well as a small artwork representing to individuals of the highlighted race."""

    console.print_frame(screen_width-38,3, 35,49)
    console.print(screen_width-37, 4,
                classes[highlighted_row-1].artwork,
                color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)



def print_traits_screen(console:Console, screen_width:int, screen_height:int, attrib_list:List[Attribute], highlighted_row:int, player_mods:List[int]) -> None:
    """
    Prints the attributes tweaking screen using the different UI printing functions:\n
    - `...()` - ...\n
    """

    print_attributes(console, screen_width, screen_height, attrib_list, highlighted_row, player_mods)



#def switch_next_screen() -> str:
#    """Changes the screen to the next one ("Biography" screen).\n
#    Returns a string (`str`): `"BIO_SCREEN"`."""
#    return "BIO_SCREEN"