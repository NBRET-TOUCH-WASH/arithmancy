#coding:utf-8

#modules
from tcod import *

from .events import *

from assets import color_tokens

from .race import race_ui



#functions
def main_char_creation(context:context.Context, console:Console, screen_width:int, screen_height:int):
    """Main character creation segment function."""

    char_creator_event_handler = CharacterCreatorEventHandler()

    while True:
        console.clear()

        #console.print_frame(0,0, screen_width,screen_height, "Character creation")
        #console.draw_frame(0,0, screen_width,screen_height,
        #                    #"Character creation",
        #                    clear=False,
        #                    fg=color_tokens.PEARL.rgb, bg=color_tokens.BLACK.rgb,
        #                    decoration="████ ████")


        race_ui.print_races(console, screen_width, screen_height, race_ui.available_races, race_ui.highlighted_row)

        race_ui.print_info(console, screen_width, screen_height, race_ui.available_races, race_ui.highlighted_row)
        race_ui.print_feats(console,screen_width, screen_height, race_ui.available_races, race_ui.highlighted_row)
        race_ui.print_symbol(console, screen_width, screen_height, race_ui.available_races, race_ui.highlighted_row)

        #little ASCII-art related to the race
        console.print_frame(screen_width-38,3, 35,49)
        console.print(screen_width-32,4, """""")


        context.present(console)

        for current_event in event.wait():
            context.convert_event(current_event)
            print(current_event)
            action = char_creator_event_handler.dispatch(current_event)

            if action is None:
                continue
            elif isinstance(action, OptionRowChange):
                race_ui.highlighted_row += action.row_change
                race_ui.highlighted_row = race_ui.clamp_highlighted_race(race_ui.highlighted_row, race_ui.available_races)
            elif isinstance(current_event, event.Quit):
                raise SystemExit()