#coding:utf-8

"""
notes
"""



#modules
from tcod import *

from options import *

#modules init



#global variables
SCREEN_WIDTH = 115
SCREEN_HEIGHT = 65

#!path to the tileset needs to be changed accordingly
SCREEN_TILESET = tileset.load_tilesheet(R"..\..\assets\tilesheet160x160.png", 16,16, tileset.CHARMAP_CP437)

MAIN_CONSOLE = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'F')


#the list of options printed on the screen
main_list = Options(MAIN_CONSOLE,)

"""
? the following list only serves to check whether or not the frame
? adapts its dimensions accordingly
* main_list = Options(MAIN_CONSOLE,
*                     [
*                         "Cool option",
*                         "Even cooler option",
*                         "The coolest of options",
*                         "Just kidding this one's the coolest",
*                         "☺ The shittiest of options ☻"
*                     ])
"""



#functions
def main():
    """The main function.\n
    Creates the main `context`, `terminal` and `console` used during execution.\n
    Returns nothing.
    """

    with context.new(columns=MAIN_CONSOLE.width, rows=MAIN_CONSOLE.height, tileset=SCREEN_TILESET, title="Arithmancy") as MAIN_CONTEXT:
        selected_row = 1
        while True:
            MAIN_CONSOLE.clear()

            MAIN_CONSOLE.draw_frame((SCREEN_WIDTH//2) - main_list.width//2,
                                    (SCREEN_HEIGHT//2) - main_list.height//2,
                                    main_list.width,
                                    main_list.height)


            #the row on which the "next" option text is printed on
            row = 1
            for opt in main_list.options:
                #if the currently printed row is the one "selected" by the user, highlight it
                if row == selected_row:
                    MAIN_CONSOLE.print((SCREEN_WIDTH//2) - len(opt)//2,
                                    (SCREEN_HEIGHT//2) - main_list.height//2 + row + 2,
                                    opt, (0,0,0), (255,255,255))

                #if the currently printed row is not the one "selected" by the user, do not highlight it
                else:
                    MAIN_CONSOLE.print((SCREEN_WIDTH//2) - len(opt)//2,
                                    (SCREEN_HEIGHT//2) - main_list.height//2 + row + 2,
                                    opt)
                row += 1


            #Displays changes; is required to see any new stuff.
            MAIN_CONTEXT.present(MAIN_CONSOLE)


            #event handling
            for current_event in event.wait():
                MAIN_CONTEXT.convert_event(current_event)
                print(current_event)

                if isinstance(current_event, event.KeyDown) and current_event.sym == event.KeySym.DOWN:
                    selected_row += 1
                    if selected_row > len(main_list.options):
                        selected_row = len(main_list.options)
                    print(selected_row)
                elif isinstance(current_event, event.KeyDown) and current_event.sym == event.KeySym.UP:
                    selected_row -= 1
                    if selected_row < 1:
                        selected_row = 1
                    print(selected_row)
                elif isinstance(current_event, event.Quit):
                    raise SystemExit()



#directives
if __name__ == "__main__":
    main()