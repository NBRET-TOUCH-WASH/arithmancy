#coding:utf-8

"""
notes
    ? docs
        ? this file serves as an example to get several windows up
        ? containing different types of informations at the same time
"""



#modules
from tcod import *

from entities import *

#modules init



#global variables
SCREEN_WIDTH = 115
SCREEN_HEIGHT = 65

#!path to the tileset needs to be changed accordingly
SCREEN_TILESET = tileset.load_tilesheet(R"..\..\assets\tilesheet160x160.png", 16,16, tileset.CHARMAP_CP437)

MAIN_CONSOLE = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'F')



#functions
def main():
    """The main function.\n
    Creates the main `context`, `terminal` and `console` used during execution.\n
    Returns nothing.
    """

    player_states = {
            "ablaze":False,
            "asleep":False,
            "blind":False,
            "confused":False,
            "hexed":False,
            "poisoned":False
        }
    test_player = Player("John Place", 100,80, 69, player_states, "Warlord")

    with context.new(columns=MAIN_CONSOLE.width, rows=MAIN_CONSOLE.height, tileset=SCREEN_TILESET, title="Arithmancy") as MAIN_CONTEXT:
        while True:
            MAIN_CONSOLE.clear()

            MAIN_CONSOLE.draw_frame(SCREEN_WIDTH-21,0, SCREEN_WIDTH-(SCREEN_WIDTH-21),SCREEN_HEIGHT-20, "Player Stats")
            MAIN_CONSOLE.print(SCREEN_WIDTH-19,5, f"Name : {test_player.name}\nTitle: {test_player.title}\nLVL  : {test_player.level}\nHP   : {test_player.hp}\nMP   : {test_player.mp}")
            for state in test_player.states.values():
                MAIN_CONSOLE.print(SCREEN_WIDTH-19,15, f"eef:{state}")

            MAIN_CONTEXT.present(MAIN_CONSOLE)


            for current_event in event.wait():
                MAIN_CONTEXT.convert_event(current_event)
                print(current_event)

                if isinstance(current_event, event.Quit):
                    raise SystemExit()



#directives
if __name__ == "__main__":
    main()