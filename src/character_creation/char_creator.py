#coding:utf-8

#modules
from tcod import *

from .events import *

from assets import color_tokens

from .screens import *
from public import data
from .bio.player_names import names

from .race import race_ui
from .bio import bio_ui



#functions
def main_char_creation(context:context.Context, console:Console, screen_width:int, screen_height:int):
    """Main character creation segment function."""

    char_creator_event_handler = CharacterCreatorEventHandler()
    CHAR_CURRENT_SCREEN:str = "RACE_SCREEN"

    while True:
        console.clear()

        if CHAR_CURRENT_SCREEN == "RACE_SCREEN":
            race_ui.print_race_selection_screen(console, screen_width, screen_height, race_ui.available_races, race_ui.highlighted_row)
        elif CHAR_CURRENT_SCREEN == "BIO_SCREEN":
            #TODO: make this cleaner with the use of text input
            if bio_ui.IS_NAME_SELECTED == False:
                data.player_data["bio"]["name"] = bio_ui.get_random_name(names.player_names)
                data.export_json_char(data.player_data)
                bio_ui.IS_NAME_SELECTED = True

            bio_ui.print_bio_screen(console, screen_width, screen_height)

        context.present(console)


        for current_event in event.wait():
            context.convert_event(current_event)
            print(current_event)
            action = char_creator_event_handler.dispatch(current_event)

            if action is None:
                continue

            elif isinstance(action, OptionRowChange):
                if CHAR_CURRENT_SCREEN == "RACE_SCREEN":
                    race_ui.highlighted_row += action.row_change
                    race_ui.highlighted_row = race_ui.clamp_highlighted_race(race_ui.highlighted_row, race_ui.available_races)

            elif isinstance(action, Submit):
                if CHAR_CURRENT_SCREEN == "RACE_SCREEN":
                    data.save_char_data(data.player_data, "race", race_ui.available_races[race_ui.highlighted_row-1].name)
                    data.export_json_char(data.player_data)
                    CHAR_CURRENT_SCREEN = switch_screen(CHAR_CURRENT_SCREEN)

            elif isinstance(current_event, event.Quit):
                raise SystemExit()