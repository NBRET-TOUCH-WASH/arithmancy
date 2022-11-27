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

import private.cli_args.arg_parsing as arg_parsing

import assets.color_tokens as color_tokens

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
        main_console.print(0,0,"bruh‼", color_tokens.FUSCHIA.rgb, color_tokens.BLACK.rgb)

        #Displays changes; is required to see any new stuff.
        main_context.present(main_console)


        #event handling
        for current_event in event.wait():
            #TODO: refactor when splitting CLI args parsing to modules
            try:
                if arg_parsing.cli_args.verbose:
                    print(current_event)
            except AttributeError:
                pass

            main_context.convert_event(current_event)

            if isinstance(current_event, event.Quit):
                raise SystemExit()



#directives
if __name__ == "__main__":
    main_gameplay()