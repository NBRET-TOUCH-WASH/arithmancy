#coding:utf-8

"""
notes
    ? docs
        ? this file serves as a template to get a basic window up
        ? and running (tailored to the needs) of the Arithmancy project

        ? this file was written after the file found on the the tcod library documentation's website
        ? ( https://python-tcod.readthedocs.io/en/latest/tcod/getting-started.html )
"""



#modules
from tcod import *

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

    with context.new(columns=MAIN_CONSOLE.width, rows=MAIN_CONSOLE.height, tileset=SCREEN_TILESET, title="Arithmancy") as MAIN_CONTEXT:
        while True:
            MAIN_CONSOLE.clear()

            # ===================== #
            # Printing goes here...
            # ===================== #

            #Displays changes; is required to see any new stuff.
            MAIN_CONTEXT.present(MAIN_CONSOLE)


            #event handling
            for current_event in event.wait():
                MAIN_CONTEXT.convert_event(current_event)
                print(current_event)

                if isinstance(current_event, event.Quit):
                    raise SystemExit()



#directives
if __name__ == "__main__":
    main()