#coding:utf-8

#type hinting
from typing import List, Dict
from tcod import Console




#modules
from importlib import import_module

from assets import color_tokens
from .class_derived import *



#classes/instances
mage_class = Mage()
necromancer_class = Necromancer()
cleric_class = Cleric()
warrior_class = Warrior()


#the different classes showed up on screen
available_classes:List[CharCreationClass] = [
    mage_class,
    necromancer_class,
    cleric_class,
    warrior_class
]



#variables
highlighted_row:int = 1

attrib_mods:Dict[str, int] = {
    "bruh":0
}

def clamp_highlighted_class(highlight:int, classes:List[CharCreationClass]) -> None:
    """Clamps the class highlight in the range of the available classes list.\n
    Returns nothing (`None`)."""
    if highlight < 1:
        return 1
    elif highlight > len(classes):
        return len(classes)
    else:
        return highlight



#functions
def print_classes(console:Console, screen_width:int, screen_height:int, classes:List[CharCreationClass], highlighted_row:int) -> None:
    """Prints the different available races to select as well as a small prompt.\n
    Returns nothing (`None`)."""

    printed_row = 1
    for r in range(len(available_classes)):
        if printed_row == highlighted_row:
            console.print(3, 5+printed_row,
                        classes[r].name,
                        color_tokens.WHITE.rgb,color_tokens.BLACK.rgb)
        else:
            console.print(3, 5+printed_row,
                        classes[r].name,
                        color_tokens.CHARCOAL.rgb, color_tokens.BLACK.rgb)
        printed_row += 1


    console.print(3,3, "Select your character's class:", color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)



def print_info(console:Console, screen_width:int, screen_height:int, classes:List[CharCreationClass], highlighted_row:int):
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



def print_attributes_mods(console:Console, screen_width:int, screen_height:int, classes:List[CharCreationClass], highlighted_row:int):
    """Prints a symbol box-frame as well as the list of racial feats corresponding to the highlighted race."""

    console.print_frame(screen_width-76,15, 35,37, "Attributes modifiers")

    highlighted_class = classes[highlighted_row-1]
    mods_list:List[CharCreationClass] = highlighted_class.attributes_modifiers

    row = 19
    for mod in mods_list:
        console.print(screen_width-74, row,
                            #33, 35,
                            mod[0],
                            color_tokens.WHITE.rgb)
        lines = console.print(screen_width-45, row,
                            mod[1],
                            highlighted_class.mod_types[mod[2]].rgb,
                            color_tokens.BLACK.rgb)
        row += 7
        #row += 6



def print_color(console:Console, screen_width:int, screen_height:int, classes:List[CharCreationClass], highlighted_row:int, player_symbol:str):
    """Prints a symbol box-frame as well as the symbol representing to individuals of the highlighted race."""

    console.print_frame(screen_width-91,3, 26,10, "Class-specific color")
    console.print((screen_width-91+26//2) - len(player_symbol)//2, 3+10//2,
                player_symbol,
                classes[highlighted_row-1].color, color_tokens.BLACK.rgb)



def print_artwork(console:Console, screen_width:int, screen_height:int, classes:List[CharCreationClass], highlighted_row:int):
    """Prints an artwork box-frame as well as a small artwork representing to individuals of the highlighted race."""

    console.print_frame(screen_width-38,3, 35,49)
    console.print(screen_width-37, 4,
                classes[highlighted_row-1].artwork,
                color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)



def print_class_selection_screen(console:Console, screen_width:int, screen_height:int, classes:List[CharCreationClass], highlighted_row:int, player_symbol:str) -> None:
    """
    Prints the race selection screen using the different UI printing functions:\n
    - `print_classes()` - Prints a list of available character classes\n
    - `print_info()` - Prints info regarding the highlighted character class\n
    - `print_attributes_mods()` - Prints the highlighted character class' attributes modifiers\n
    - `print_symbol()` - Prints the highlighted character class' attributes modifiers\n
    """

    print_classes(console, screen_width, screen_height, classes, highlighted_row)
    print_info(console, screen_width, screen_height, classes, highlighted_row)
    print_attributes_mods(console, screen_width, screen_height, classes, highlighted_row)
    print_color(console, screen_width, screen_height, classes, highlighted_row, player_symbol)
    print_artwork(console, screen_width, screen_height, classes, highlighted_row)



#def switch_next_screen() -> str:
#    """Changes the screen to the next one ("Biography" screen).\n
#    Returns a string (`str`): `"BIO_SCREEN"`."""
#    return "BIO_SCREEN"