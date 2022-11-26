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

import private.launch_settings as launch_settings
import assets.meta.metadata as metadata
from assets import color_tokens


from main_menu import *

from character_creation import *

from gameplay.main_gameplay import *

#modules init



#global variables
SCREEN_WIDTH = 155
SCREEN_HEIGHT = 55

#SCREEN_TILESET = tileset.load_tilesheet(R".\assets\tiles\tilesheet160x160.png", 16,16, tileset.CHARMAP_CP437)
SCREEN_TILESET = tileset.load_tilesheet(R".\assets\tiles\curses_640x300.png", 16,16, tileset.CHARMAP_CP437)

MAIN_CONSOLE = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'F')

MAIN_MENU_OPTIONS = Options(MAIN_CONSOLE)



#functions
def main():
    """The main function.\n
    Creates the main `context`, `terminal` and `console` used during execution.\n
    Returns nothing.
    """

    #event handlers
    main_menu_event_handler = MainMenuEventHandler()
    options_screen_event_handler = OptionsScreenEventHandler()
    about_screen_event_handler = AboutScreenEventHandler()

    char_creator_event_handler = CharacterCreatorEventHandler()


    with context.new(columns=MAIN_CONSOLE.width, rows=MAIN_CONSOLE.height, tileset=SCREEN_TILESET, title=f"Arithmancy {metadata.VERSION_TAG}") as MAIN_CONTEXT:
        MAIN_MENU_OPTIONS_SELECTED_ROW = 1
        CURRENT_SCREEN = "MAIN_MENU"
        while True:
            MAIN_CONSOLE.clear()

            if CURRENT_SCREEN == "MAIN_MENU":
                print_main_menu(MAIN_CONSOLE, SCREEN_WIDTH,SCREEN_HEIGHT,
                                            metadata.AUTHOR, metadata.DATE, metadata.LICENSE, metadata.VERSION_TAG,
                                            color_tokens.WHITE.rgb, color_tokens.BLACK.rgb,
                                            color_tokens.VIOLET.rgb, color_tokens.AQUA.rgb, color_tokens.CRIMSON.rgb)
                MAIN_MENU_OPTIONS.print_options(MAIN_CONSOLE, SCREEN_WIDTH,SCREEN_HEIGHT, MAIN_MENU_OPTIONS_SELECTED_ROW)

                if launch_settings.DEBUG:#? has no real use right now but probably will in the future
                    MAIN_CONSOLE.print(SCREEN_WIDTH-20,SCREEN_HEIGHT-4,"☼ DEBUG MODE ☼", color_tokens.FUSCHIA.rgb)

            elif CURRENT_SCREEN == "ABOUT_SCREEN":
                print_about_screen(MAIN_CONSOLE, SCREEN_WIDTH, SCREEN_HEIGHT,
                                                color_tokens.WHITE.rgb, color_tokens.BLACK.rgb, color_tokens.CHARTREUSE.rgb)

            elif CURRENT_SCREEN == "OPTIONS_SCREEN":
                print_options_screen(MAIN_CONSOLE, SCREEN_WIDTH, SCREEN_HEIGHT,
                                                color_tokens.WHITE.rgb, color_tokens.BLACK.rgb, color_tokens.CHARTREUSE.rgb)

            if CURRENT_SCREEN == "START_GAMEPLAY":
                main_gameplay(MAIN_CONTEXT, MAIN_CONSOLE, SCREEN_WIDTH, SCREEN_HEIGHT)

            #Displays changes; is required to see any new stuff.
            MAIN_CONTEXT.present(MAIN_CONSOLE)


            #event handling
            for current_event in event.wait():
                MAIN_CONTEXT.convert_event(current_event)
                print(current_event)

                #event dispatching
                if CURRENT_SCREEN == "MAIN_MENU":
                    action = main_menu_event_handler.dispatch(current_event)
                elif CURRENT_SCREEN == "OPTIONS_SCREEN":
                    action = options_screen_event_handler.dispatch(current_event)
                elif CURRENT_SCREEN == "ABOUT_SCREEN":
                    action = about_screen_event_handler.dispatch(current_event)
                elif CURRENT_SCREEN == "EXIT_GAME":
                    raise SystemExit()

                elif CURRENT_SCREEN == "INIT_GAME":
                    char_creator.main_char_creation(MAIN_CONTEXT, MAIN_CONSOLE, SCREEN_WIDTH, SCREEN_HEIGHT)
                    CURRENT_SCREEN = char_creator.end_character_creation()
                    break #dunno why this works but okay


                if action is None:
                    continue

                if isinstance(action, MainMenuOptionAction):
                    MAIN_MENU_OPTIONS_SELECTED_ROW += action.row_change
                    if MAIN_MENU_OPTIONS_SELECTED_ROW > len(MAIN_MENU_OPTIONS.options):
                        MAIN_MENU_OPTIONS_SELECTED_ROW = len(MAIN_MENU_OPTIONS.options)
                    elif MAIN_MENU_OPTIONS_SELECTED_ROW < 1:
                        MAIN_MENU_OPTIONS_SELECTED_ROW = 1

                elif isinstance(action, MainMenuOptionSelection):
                    CURRENT_SCREEN = change_screen(MAIN_MENU_OPTIONS_SELECTED_ROW)
                elif isinstance(action, OptionsScreenGoBack):
                    CURRENT_SCREEN = "MAIN_MENU"
                elif isinstance(action, AboutScreenGoBack):
                    CURRENT_SCREEN = "MAIN_MENU"

                elif isinstance(current_event, event.Quit):
                    raise SystemExit()



#directives
if __name__ == "__main__":
    main()