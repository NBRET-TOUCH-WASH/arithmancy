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



#functions
def main_gameplay(main_context:context.Context, main_console:Console, screen_width:int, screen_height:int):
    """The main gameplay function.\n
    Creates the main `context`, `terminal` and `console` for the main gameplay section.\n
    Returns ??? (`???`).
    """

    while True:
        main_console.clear()

        # ===================== #
        # Printing goes here...
        # ===================== #

        #Displays changes; is required to see any new stuff.
        main_context.present(main_console)


        #event handling
        for current_event in event.wait():
            main_context.convert_event(current_event)
            print(current_event)

            if isinstance(current_event, event.Quit):
                raise SystemExit()



#directives
if __name__ == "__main__":
    main_gameplay()