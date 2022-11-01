#coding:utf-8

"""
       .==.          .==.
     / ^ ^ \        / ^ ^ \
    / ^ ^ ^ \(\__/)/ ^ ^ ^ \
   /   ^ ^    6  6    ^ ^   \
  /  ^ ^ ^   ( .. )   ^ ^ ^  \
 /  ^ ^ ^ ^ / v""v \ ^ ^ ^ ^  \
/  ^ ^ ^ ^  \ `~~` /  ^ ^ ^ ^  \
================================
         HERE BE DRAGONS
"""



#modules
from tcod import *

import assets.meta.metadata as metadata
from assets import color_tokens
import main_menu

#modules init



#global variables
SCREEN_WIDTH = 155
SCREEN_HEIGHT = 55

#SCREEN_TILESET = tileset.load_tilesheet(R".\assets\tiles\tilesheet160x160.png", 16,16, tileset.CHARMAP_CP437)
SCREEN_TILESET = tileset.load_tilesheet(R".\assets\tiles\curses_640x300.png", 16,16, tileset.CHARMAP_CP437)

MAIN_CONSOLE = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'F')

MAIN_MENU_OPTIONS = main_menu.Options(MAIN_CONSOLE)

#functions
def main():
    """The main function.\n
    Creates the main `context`, `terminal` and `console` used during execution.\n
    Returns nothing.
    """

    with context.new(columns=MAIN_CONSOLE.width, rows=MAIN_CONSOLE.height, tileset=SCREEN_TILESET, title="Arithmancy") as MAIN_CONTEXT:
        MAIN_MENU_OPTIONS_SELECTED_ROW = 1
        while True:
            MAIN_CONSOLE.clear()

            main_menu.print_main_menu(MAIN_CONSOLE, SCREEN_WIDTH,
                                    color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
            MAIN_MENU_OPTIONS.print_options(MAIN_CONSOLE,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            MAIN_MENU_OPTIONS_SELECTED_ROW)
            main_menu.print_condensed_credits(MAIN_CONSOLE, SCREEN_HEIGHT,
                                            metadata.AUTHOR, metadata.YEAR, metadata.LICENSE,
                                            color_tokens.WHITE.rgb, color_tokens.VIOLET.rgb, color_tokens.AQUA.rgb)
            main_menu.print_version_tag(MAIN_CONSOLE, SCREEN_WIDTH, SCREEN_HEIGHT, metadata.VERSION_TAG, color_tokens.CRIMSON.rgb)

            #Displays changes; is required to see any new stuff.
            MAIN_CONTEXT.present(MAIN_CONSOLE)


            #event handling
            for current_event in event.wait():
                MAIN_CONTEXT.convert_event(current_event)
                print(current_event)

                if isinstance(current_event, event.KeyDown) and current_event.sym == event.KeySym.DOWN:
                    MAIN_MENU_OPTIONS_SELECTED_ROW += 1
                    if MAIN_MENU_OPTIONS_SELECTED_ROW > len(MAIN_MENU_OPTIONS.options):
                        MAIN_MENU_OPTIONS_SELECTED_ROW = len(MAIN_MENU_OPTIONS.options)
                    print(f"Current option row: {MAIN_MENU_OPTIONS_SELECTED_ROW}")

                elif isinstance(current_event, event.KeyDown) and current_event.sym == event.KeySym.UP:
                    MAIN_MENU_OPTIONS_SELECTED_ROW -= 1
                    if MAIN_MENU_OPTIONS_SELECTED_ROW < 1:
                        MAIN_MENU_OPTIONS_SELECTED_ROW = 1
                    print(f"Current option row: {MAIN_MENU_OPTIONS_SELECTED_ROW}")

                elif isinstance(current_event, event.KeyDown) and current_event.sym == event.KeySym.RETURN:
                    print(f"Selected option: \"{MAIN_MENU_OPTIONS.options[MAIN_MENU_OPTIONS_SELECTED_ROW - 1]}\"")


                if isinstance(current_event, event.Quit):
                    raise SystemExit()



#directives
if __name__ == "__main__":
    main()