#coding:utf-8

#type hinting
from typing import List, Dict
from tcod import Console
from tcod.constants import LEFT, CENTER, RIGHT




#modules
from public.data.data import player_data, player_mods
from assets import color_tokens



#classes/instances
class Attribute:
    """Represents a character attribute during the character creation segment."""
    def __init__(self) -> None:
        self.name:str = "Attribute"
        self.symbol:str = "SYM"
        self.value:int = 0
        self.description:str = "SAMPLE_TXT"

class Constitution(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.name:str = "Constitution"
        self.symbol = "CON"
        self.description = "The character's ability to resist and recover from damage received."

class Dexterity(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.name:str = "Dexterity"
        self.symbol = "DEX"
        self.description = "Combination of the character's agility and quickness."

class Intelligence(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.name:str = "Intelligence"
        self.symbol = "INT"
        self.description = "Spellcasting abilities of spellcasters from the arcane and shadow realms."

class Strength(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.name:str = "Strength"
        self.symbol = "STR"
        self.description = "Character's aw physical strength."

class Wisdom(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.name:str = "Wisdom"
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

total_points:int = 20
spent_points:int = 0



#variables
highlighted_row:int = 1

def clamp_attrib_highlight(attrib_highlight:int, attrib_list:List[Attribute]) -> None:
    """Clamps the attribute highlight in the range of the attributes list.\n
    Returns nothing (`None`)."""
    if attrib_highlight < 1:
        return 1
    elif attrib_highlight > len(attrib_list):
        return len(attrib_list)
    else:
        return attrib_highlight



#functions
def increment_attribute_value(attributes_list:List[Attribute], highlighted_attrib:int, available_points:int) -> int:
    """Increments an attribute's value according to a certain \"balance\" of points \
    (i.e. incrementing 6 goes to 8, which then goes to 12 and gets capped).\n
    Returns an integer (`int`)."""
    value = attributes_list[highlighted_attrib-1].value
    if value < 0:
        return 0
    elif 0 <= value < 6:
        return 1
    elif value == 6:
        return 2
    elif value == 8:
        return 4
    elif value >= 12 or available_points < value:
        return 0 #adds nothing zero to the value, effectively not adding anything
    else:
        raise ValueError()

def decrement_attribute_value(attributes_list:List[Attribute], highlighted_attrib:int) -> int:
    """Decrements an attribute's value according to a certain \"balance\" of points \
    (i.e. decrementing 12 goes to 8, which then goes to 6 and then by steps of one until the 0 cap).\n
    Returns an integer (`int`)."""
    value = attributes_list[highlighted_attrib-1].value
    if value == 0:
        return 0 #substracts nothing zero to the value, effectively not adding anything
    elif 0 < value <= 6:
        return 1
    elif value == 8:
        return 2
    elif value >= 12:
        return 4
    else:
        raise ValueError()

def clamp_attributes_value(attributes_list:List[Attribute], hihglighted_attrib:int) -> int:
    """Clamps the highlighted attribute's value. Currently only keeps the player from setting \
    a negative value to an attribute.\n
    Returns an integer (`int`)."""
    if attributes_list[hihglighted_attrib-1].value < 0:
        return 0
    elif attributes_list[hihglighted_attrib-1].value >= 12:
        return 12
    else:
        return attributes_list[hihglighted_attrib-1].value

def change_total_points(attribute:int, switch:int) -> int:
    """Changes the amount of points left to spend after incrementing or decrementing an attribute's value.\n
    `switch` is a flag only accepting `1` and `2` as values; respectively signaling addition or substraction.\n
    Returns an integer (`int`)."""
    #return available_points - value
    #spent_points_sum:int = 0
    #for a in range(len(attributes_list)):
    #    spent_points_sum += attributes_list[a].value
    #return available_points - spent_points_sum

    if not (switch == 1 or switch == 2):
        raise ValueError()

    if 0 <= attribute <= 5:
        return 1

    elif attribute == 6:
        if switch == 1:
            return 2
        elif switch == 2:
            return 1

    elif attribute == 8:
        if switch == 1:
            return 4
        elif switch == 2:
            return 2

    elif attribute == 12:
        if switch == 1:
            return 4
        elif switch == 2:
            return 4

    else:
        return 0

def clamp_total_points(total_points:int):
    if total_points < 0:
        return 0
    elif total_points > 20:
        return 20
    else:
        return total_points


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
            console.print(screen_third*2-2, 10+printed_row, "10 + ".format(str(attrib_list[a].value)), color_tokens.ASH.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            if ATTRIB_IS_BUFF:
                console.print(screen_third*2, 10+printed_row, "{}".format(str(attrib_list[a].value)), color_tokens.GREEN.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            elif ATTRIB_IS_NEUTRAL:
                console.print(screen_third*2, 10+printed_row, str(attrib_list[a].value), color_tokens.YELLOW.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)

            if MOD_IS_BUFF:
                console.print(screen_third*2+4, 10+printed_row, "+ {}".format(str(abs(player_mods[a]))), color_tokens.GREEN.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            elif MOD_IS_NEUTRAL:
                console.print(screen_third*2+4, 10+printed_row, "± {}".format(str(abs(player_mods[a]))), color_tokens.ASH.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            elif MOD_IS_DEBUFF:
                console.print(screen_third*2+4, 10+printed_row, "- {}".format(str(abs(player_mods[a]))), color_tokens.RED.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            #elif ATTRIB_IS_DEBUFF:
            #    console.print(screen_third*2, 10+printed_row, str(attrib_list[a].value), color_tokens.RED.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)

        else:
            console.print(screen_third, 10+printed_row,
                        attrib_list[a].symbol,
                        color_tokens.CHARCOAL.rgb, color_tokens.BLACK.rgb)
            console.print(screen_width//2,10+printed_row, "=", color_tokens.CHARCOAL.rgb, color_tokens.BLACK.rgb, alignment=CENTER)
            console.print(screen_third*2-2, 10+printed_row, "10 + ", color_tokens.TAUPE_PURPLE.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            if ATTRIB_IS_BUFF:
                console.print(screen_third*2, 10+printed_row, "{}".format(str(attrib_list[a].value)), color_tokens.DARK_GREEN.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            elif ATTRIB_IS_NEUTRAL:
                console.print(screen_third*2, 10+printed_row, str(attrib_list[a].value), color_tokens.TAUPE.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            #elif ATTRIB_IS_DEBUFF:
            #    console.print(screen_third*2, 10+printed_row, str(attrib_list[a].value), color_tokens.MAROON.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)

            if MOD_IS_BUFF:
                console.print(screen_third*2+4, 10+printed_row, "+ {}".format(str(abs(player_mods[a]))), color_tokens.DARK_GREEN.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            elif MOD_IS_NEUTRAL:
                console.print(screen_third*2+4, 10+printed_row, "± {}".format(str(abs(player_mods[a]))), color_tokens.TAUPE_PURPLE.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
            elif MOD_IS_DEBUFF:
                console.print(screen_third*2+4, 10+printed_row, "- {}".format(str(abs(player_mods[a]))), color_tokens.MAROON.rgb, color_tokens.BLACK.rgb, alignment=RIGHT)
        printed_row += 1


    console.print(3,3, "Tweak your character's attributes to your liking:", color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
    console.print(screen_width//2,screen_height-7, "Press the [UP] and [DOWN] arrow keys to raise or lower the attribute highlight.", color_tokens.FERN_GREEN.rgb, color_tokens.BLACK.rgb, alignment=CENTER)
    console.print(screen_width//2,screen_height-6, "Press the [+] and [-] keys on your keyboard to increment or decrement the highlighted attribute.", color_tokens.FERN_GREEN.rgb, color_tokens.BLACK.rgb, alignment=CENTER)
    console.print(screen_width//2,screen_height-4, "Press [ENTER] to submit your choices and finish character creation.", color_tokens.FERN_GREEN.rgb, color_tokens.BLACK.rgb, alignment=CENTER)



#def print_info(console:Console, screen_width:int, screen_height:int, attrib_list:List[Attribute], highlighted_row:int):
#    """Prints an info box-frame as well as a relatively short description of the highlighted race."""

#    console.print_frame(screen_width-113,15,
#                        35,37,
#                        "Info")

#    #console.print(screen_width-112,16,
#    #            races[highlighted_row].info,
#    #            color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
#    console.print_rect(screen_width-111+31//2, 17,
#                        31,36,
#                        classes[highlighted_row-1].info,
#                        alignment=2)



def print_points_left(console:Console, screen_width:int, screen_height:int, attrib_list:List[Attribute], highlighted_row:int, points_left:int):
    """Prints the amount of points left to spend on attributes."""

    console.draw_frame(screen_width-36,screen_height//2-10, 31,20, decoration="╔═╗║ ║╚═╝")
    console.print(screen_width-36+30//2, screen_height//2-8, "Points left to spend:", color_tokens.WHITE.rgb, color_tokens.BLACK.rgb, alignment=CENTER)
    console.print(screen_width-36+32//2, screen_height//2-5, str(points_left), color_tokens.GOLDEN_YELLOW.rgb, color_tokens.BLACK.rgb, alignment=CENTER)
    console.print_rect(screen_width-36+30//2, screen_height//2+5, 29,5, "Points can be spent to increment or decrement your character's attributes.", alignment=CENTER)



def print_traits_screen(console:Console, screen_width:int, screen_height:int, attrib_list:List[Attribute], highlighted_row:int, player_mods:List[int], points_left:int) -> None:
    """
    Prints the attributes tweaking screen using the different UI printing functions:\n
    - `...()` - ...\n
    """

    print_attributes(console, screen_width, screen_height, attrib_list, highlighted_row, player_mods)
    print_points_left(console, screen_width, screen_height, attrib_list, highlighted_row, points_left)



#def switch_next_screen() -> str:
#    """Changes the screen to the next one ("Biography" screen).\n
#    Returns a string (`str`): `"BIO_SCREEN"`."""
#    return "BIO_SCREEN"