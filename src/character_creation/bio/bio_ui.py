#coding:utf-8

#type hinting
from typing import List, Tuple
from random import randint

from tcod import Console

from assets import color_tokens
from public.data import data

#modules

#variables
IS_NAME_SELECTED:bool = False

#functions
def get_random_name(names_list:List[Tuple[str, str]]) -> str:
    while True:
        random_index:int = randint(0, len(names_list)-1)
        if names_list[random_index][0] == data.player_data["race"]:
            break
        else:
            continue
    return names_list[random_index][1]



def print_bio_ui(console:Console, screen_width:int, screen_height:int, player_name:str):
    #console.draw_frame(screen_width//2-(len(player_name)//2)*2, screen_height//4,
    #                    13, 5,
    #                    "Firstname",
    #                    True,
    #                    color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
    console.print(screen_width//2-30//2, screen_height//4,
                "Randomly selected player name:",
                color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
    console.print(screen_width//2-len(player_name)//2, screen_height//4+2,
                player_name,
                color_tokens.HELIOTROPE.rgb, color_tokens.BLACK.rgb)



def print_bio_screen(console:Console, screen_width:int, screen_height:int) -> None:
    """
    Prints the biography screen using the different UI printing functions:\n
    - `...()` - ...\n
    """

    #selected_player_name = get_random_name(player_race, names.player_names)
    print_bio_ui(console, screen_width, screen_height, data.player_data["bio"]["name"])