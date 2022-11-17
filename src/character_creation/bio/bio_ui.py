#coding:utf-8

#type hinting
from typing import List, Tuple
from random import randint

from tcod import Console
from tcod.constants import LEFT, CENTER, RIGHT

from assets import color_tokens
from public.data import data

#modules

#variables
IS_NAME_SELECTED:bool = False

#by alphabetical order so no one can complain :)
#builtin_genders = ["♂", "♀", "○"] currently unable to get the enby symbol, only the agender one :/
#builtin_genders = ["Enby", "Female", "Male"]
#highlighted_gender_column:int = 155//5

#functions
#def clamp_highlighted_gender(screen_width:int, highlight:int, genders:List[str]) -> None:
#    """Clamps the gender highlight in the range of the builtin genders list.\n
#    Returns nothing (`None`)."""

#    column = screen_width//5
#    if highlight < column:
#        return column
#    elif highlight > column*len(genders):
#        return column*len(genders)

#    else:
#        return highlight


def get_random_name(names_list:List[Tuple[str, str]]) -> str:
    while True:
        random_index:int = randint(0, len(names_list)-1)
        if names_list[random_index][0] == data.player_data["race"]:
            break
        else:
            continue
    return names_list[random_index][1]



def print_name(console:Console, screen_width:int, screen_height:int, player_name:str) -> None:
    """
    Prints a randomly-picked name based on the character's previously selected race.\n
    Needs to be rewritten when text input is correctly handled.\n
    Returns nothing (`None`).
    """
    #console.draw_frame(screen_width//2-(len(player_name)//2)*2, screen_height//4,
    #                    13, 5,
    #                    "Firstname",
    #                    True,
    #                    color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
    console.print(screen_width//2, screen_height//4,
                "Randomly selected player name:",
                color_tokens.WHITE.rgb, color_tokens.BLACK.rgb,
                alignment=CENTER)
    console.print(screen_width//2, screen_height//4+2,
                player_name,
                color_tokens.HELIOTROPE.rgb, color_tokens.BLACK.rgb,
                alignment=CENTER)

    console.print(screen_width//2, screen_height-5,
                "Press [SPACEBAR] to advance to class selection.",
                color_tokens.DARK_OLIVE.rgb, color_tokens.BLACK.rgb,
                alignment=CENTER)


#def print_genders(console:Console, screen_width:int, screen_height:int, builtin_genders:List[str], highlighted_gender_column:int):
#    column = screen_width//5
#    #builtin_genders = {"Enby":column, "Female":column*2, "Male":column*3}
    
#    for g in range(0,len(builtin_genders)):
#        if column == highlighted_gender_column:
#            console.print(column-len(builtin_genders[g])//2, screen_height-10, builtin_genders[g], color_tokens.BLACK.rgb, color_tokens.WHITE.rgb)
#        else:
#            console.print(column-len(builtin_genders[g])//2, screen_height-10, builtin_genders[g], color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
#        column += screen_width//5

#    console.print(screen_width-screen_width//5-17//2, screen_height-10, "☼ UNIMPLEMENTED ☼", color_tokens.RED_PURPLE.rgb)



def print_bio_screen(console:Console, screen_width:int, screen_height:int) -> None:
    """
    Prints the biography screen using the different UI printing functions:\n
    - `...()` - ...\n
    """

    #selected_player_name = get_random_name(player_race, names.player_names)
    print_name(console, screen_width, screen_height, data.player_data["bio"]["name"])
    #print_genders(console, screen_width, screen_height, builtin_genders, highlighted_gender_column)