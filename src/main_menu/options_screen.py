#coding:utf-8

#type checking
from tcod import Console
from tcod import constants

#global variables
OPTIONS_SCREEN_HEADER = """
   ____                                                     
  6MMMMb                    68b                             
 8P    Y8             /     Y89                             
6M      Mb __ ____   /M     ___   _____  ___  __     ____   
MM      MM `M6MMMMb /MMMMM  `MM  6MMMMMb `MM 6MMb   6MMMMb\ 
MM      MM  MM'  `Mb MM      MM 6M'   `Mb MMM9 `Mb MM'    ` 
MM      MM  MM    MM MM      MM MM     MM MM'   MM YM.      
MM      MM  MM    MM MM      MM MM     MM MM    MM  YMMMMb  
YM      M9  MM    MM MM      MM MM     MM MM    MM      `Mb 
 8b    d8   MM.  ,M9 YM.  ,  MM YM.   ,M9 MM    MM L    ,MM 
  YMMMM9    MMYMMM9   YMMM9 _MM_ YMMMMM9 _MM_  _MM_MYMMMM9  
            MM                                              
            MM                                              
           _MM_                                             
"""

OPTIONS_SCREEN_HEADER_WIDTH = 60 #hardcoded but i don't think the header will change so it's fine

OPTIONS_SCREEN_TEXT = "This time you said \"make game not fast\", so game make not fast, and game good.\nBut still no options.\n- me ☺ -"


#functions
def print_options_screen_header(console:Console, screen_width:int, fg, bg) -> None:
    console.print(screen_width//2 - OPTIONS_SCREEN_HEADER_WIDTH//2, 3,
                    OPTIONS_SCREEN_HEADER,
                    fg,bg)

def print_options_screen_text(console:Console, screen_width:int,screen_height:int, fg,bg) -> None:
    console.print(screen_width//2, screen_height//2,
                    OPTIONS_SCREEN_TEXT,
                    fg,bg,
                    alignment=constants.CENTER)

def print_options_screen_controls(console:Console, screen_width:int, screen_height:int, fg,bg, control_color) -> None:
    console.print(screen_width//2, screen_height-10,
                    "Press [Escape] to return to the main menu",
                    control_color,bg,
                    alignment=constants.CENTER)


def print_options_screen(console:Console, screen_width,screen_height:int, fg,bg, control_color) -> None:
    print_options_screen_header(console, screen_width, fg,bg)
    print_options_screen_text(console, screen_width, screen_height, fg,bg)
    print_options_screen_controls(console, screen_width, screen_height, fg,bg, control_color)