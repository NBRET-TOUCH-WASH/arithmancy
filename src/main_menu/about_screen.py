#coding:utf-8

#type checking
from tcod import Console
from tcod import constants

#global variables
ABOUT_SCREEN_HEADER = """
       _     ___                                  
      dM.     MM                                  
     ,MMb     MM                            /     
     d'YM.    MM____     _____  ___   ___  /M     
    ,P `Mb    MMMMMMb   6MMMMMb `MM    MM /MMMMM  
    d'  YM.   MM'  `Mb 6M'   `Mb MM    MM  MM     
   ,P   `Mb   MM    MM MM     MM MM    MM  MM     
   d'    YM.  MM    MM MM     MM MM    MM  MM     
  ,MMMMMMMMb  MM    MM MM     MM MM    MM  MM     
  d'      YM. MM.  ,M9 YM.   ,M9 YM.   MM  YM.  , 
_dM_     _dMM_MYMMMM9   YMMMMM9   YMMM9MM_  YMMM9 
"""

ABOUT_SCREEN_HEADER_WIDTH = 50 #hardcoded but i don't think the header will change so it's fine

ABOUT_SCREEN_TEXT = "\"Allan, please add detail.\" [sic]\nTODO: add a witty and emotional text about the making of this project"


#functions
def print_about_screen_header(console:Console, screen_width:int, fg, bg) -> None:
    console.print(screen_width//2 - ABOUT_SCREEN_HEADER_WIDTH//2, 3,
                    ABOUT_SCREEN_HEADER,
                    fg,bg)

def print_about_screen_text(console:Console, screen_width:int,screen_height:int, fg,bg) -> None:
    console.print(screen_width//2, screen_height//2,
                    ABOUT_SCREEN_TEXT,
                    fg,bg,
                    alignment=constants.CENTER)

def print_about_screen_controls(console:Console, screen_width:int, screen_height:int, fg,bg, control_color) -> None:
    console.print(screen_width//2, screen_height-10,
                    "Press [Escape] to return to the main menu",
                    control_color,bg,
                    alignment=constants.CENTER)


def print_about_screen(console:Console, screen_width,screen_height:int, fg,bg, control_color) -> None:
    print_about_screen_header(console, screen_width, fg,bg)
    print_about_screen_text(console, screen_width, screen_height, fg,bg)
    print_about_screen_controls(console, screen_width, screen_height, fg,bg, control_color)