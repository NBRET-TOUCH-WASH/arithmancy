#coding:utf-8

#type checking
from typing import Tuple

from tcod import Console

#from assets.color_tokens.color_token import Color



#global variables
MAIN_MENU_HEADER:str = R"""
                                   ___                                             _____     ___ 
                       68b         `MM                                             `YMM`     `M' 
  ,88888888b           Y89   /      MM                                               YMM`    d'  
 68        `b  ___  __ ___  /M      MM  __  ___  __    __      ___   ___  __     ____ YMM`  d'   
,P   o68b69 Yb `MM 6MM `MM /MMMMM   MM 6MMb `MM 6MMb  6MMb   6MMMMb  `MM 6MMb   6MMMMb.YMM`d'    
6'  M'  ,M'  8  MM69 "  MM  MM      MMM9 `Mb MM69 `MM69 `Mb 8M'  `Mb  MMM9 `Mb 6M'   Mb YMM'     
M  dP   dP   8  MM'     MM  MM      MM'   MM MM'   MM'   MM     ,oMM  MM'   MM MM    `'  MM      
M ,M'  ,M'   8  MM      MM  MM      MM    MM MM    MM    MM ,6MM9'MM  MM    MM MM      MMMMMM    
M dP   dP   ,8  MM      MM  MM      MM    MM MM    MM    MM MM'   MM  MM    MM MM        MM      
M Yb  ,M'  d8'  MM      MM  YM.  ,  MM    MM MM    MM    MM MM.  ,MM  MM    MM YM.   d9  MM      
Y  YMM9Yoo6'   _MM_    _MM_  YMMM9 _MM_  _MM_MM_  _MM_  _MM_`YMMM9'Yb_MM_  _MM_ YMMMM9  _MM_     
`b                                                                                               
 `Y888888'                                                                                       
"""

MAIN_MENU_HEADER_WIDTH = 97 #hardcoded but i don't think the header will change so it's fine


#functions
#transversal
def change_screen(option_row:int):
    """Changes the main menu to the according screen.\n
    Is semi-hardcoded but fuck it."""
    if option_row == 1:
        return "INIT_GAME"
    if option_row == 2:
        return "ABOUT_SCREEN"
    if option_row == 3:
        return "OPTIONS_SCREEN"
    if option_row == 4:
        return "EXIT_GAME"



#main menu
def print_main_menu_header(console:Console, screen_width:int, fg, bg) -> None:
    console.print(screen_width//2 - MAIN_MENU_HEADER_WIDTH//2, 3,
                    MAIN_MENU_HEADER,
                    fg,bg)

#TODO: clean this up
def print_condensed_credits(console:Console, screen_height:int,
                            author:str, year:str, license:str,
                            std_color, author_accent_color, license_accent_color) -> None:
    """Prints a condensed form of the game's credits.\n
    Returns nothing (`None`).\n
    [!] Needs to be rewritten as not to be fully hardcoded [!]"""

    console.print(3, screen_height-5,
                "Created by ", std_color,(0,0,0))
    console.print(14, screen_height-5,
                author, author_accent_color,(0,0,0))
    console.print(30, screen_height-5,
                f", {year}", std_color,(0,0,0))

    console.print(3, screen_height-4,
                "Licensed under ", std_color,(0,0,0))
    console.print(18, screen_height-4,
                license, license_accent_color,(0,0,0))

def print_version_tag(console:Console, screen_width:int, screen_height:int, version_tag:str, accent_color):
    console.print(screen_width-15 - len(version_tag)//2, screen_height-5,
                    version_tag,
                    accent_color)

def print_main_menu(console:Console, screen_width:int,screen_height:int,
                    author:str, date:str, license:str, version_tag:str,
                    std_fg_color, std_bg_color, author_color, license_color, tag_color) -> None:
    print_main_menu_header(console, screen_width, std_fg_color,std_bg_color)
    print_condensed_credits(console, screen_height, author, date, license, std_fg_color, author_color, license_color)
    print_version_tag(console, screen_width, screen_height, version_tag, tag_color)