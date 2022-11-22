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
from .char_class import class_ui, class_derived
from .traits import traits_ui



#functions
def main_char_creation(context:context.Context, console:Console, screen_width:int, screen_height:int):
    """Main character creation segment function."""

    char_creator_event_handler = CharacterCreatorEventHandler()
    CHAR_CURRENT_SCREEN:str = "RACE_SCREEN"
    player_symbol:str = "SAMPLE_TEXT"

    while True:
        console.clear()

        if CHAR_CURRENT_SCREEN == "RACE_SCREEN":
            race_ui.print_race_selection_screen(console, screen_width, screen_height, race_ui.available_races, race_ui.highlighted_row)

        elif CHAR_CURRENT_SCREEN == "BIO_SCREEN":
            #TODO: make this cleaner with the use of text input
            if bio_ui.IS_NAME_SELECTED == False:
                data.player_data["bio"]["name"] = bio_ui.get_random_name(names.player_names)
                data.export_json_char(data.player_data, data.player_attributes, data.player_mods)
                bio_ui.IS_NAME_SELECTED = True
            bio_ui.print_bio_screen(console, screen_width, screen_height)

        elif CHAR_CURRENT_SCREEN == "CLASS_SCREEN":
            class_ui.print_class_selection_screen(console, screen_width, screen_height, class_ui.available_classes, class_ui.highlighted_row, player_symbol)

        elif CHAR_CURRENT_SCREEN == "TRAITS_SCREEN":
            traits_ui.print_traits_screen(console, screen_width, screen_height, traits_ui.listed_attributes, traits_ui.highlighted_row, data.player_mods, traits_ui.total_points)

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
                elif CHAR_CURRENT_SCREEN == "CLASS_SCREEN":
                    class_ui.highlighted_row += action.row_change
                    class_ui.highlighted_row = class_ui.clamp_highlighted_class(class_ui.highlighted_row, class_ui.available_classes)
                elif CHAR_CURRENT_SCREEN == "TRAITS_SCREEN":
                    traits_ui.highlighted_row += action.row_change
                    traits_ui.highlighted_row = traits_ui.clamp_attrib_highlight(traits_ui.highlighted_row, traits_ui.listed_attributes)
            elif isinstance(action, OptionColumnChange):
                if CHAR_CURRENT_SCREEN == "BIO_SCREEN":
                    bio_ui.highlighted_gender_column += action.column_change
                    bio_ui.highlighted_gender_column = bio_ui.clamp_highlighted_gender(screen_width, bio_ui.highlighted_gender_column, bio_ui.builtin_genders)
                    #bio_ui.currently_highlighted_gender = bio_ui.builtin_genders[bio_ui.highlighted_gender_column//screen_width]


            elif isinstance(action, Increment):
                if CHAR_CURRENT_SCREEN == "TRAITS_SCREEN":
                    traits_ui.listed_attributes[traits_ui.highlighted_row-1].value += traits_ui.increment_attribute_value(traits_ui.listed_attributes, traits_ui.highlighted_row)
                    traits_ui.listed_attributes[traits_ui.highlighted_row-1].value = traits_ui.clamp_attributes_value(traits_ui.listed_attributes, traits_ui.highlighted_row)
                    #traits_ui.total_points -= traits_ui.change_total_points(traits_ui.total_points, traits_ui.listed_attributes[traits_ui.highlighted_row-1].value)
                    traits_ui.total_points -= traits_ui.change_total_points(traits_ui.listed_attributes[traits_ui.highlighted_row-1].value)
            elif isinstance(action, Decrement):
                if CHAR_CURRENT_SCREEN == "TRAITS_SCREEN":
                    traits_ui.listed_attributes[traits_ui.highlighted_row-1].value -= traits_ui.decrement_attribute_value(traits_ui.listed_attributes, traits_ui.highlighted_row)
                    traits_ui.listed_attributes[traits_ui.highlighted_row-1].value = traits_ui.clamp_attributes_value(traits_ui.listed_attributes, traits_ui.highlighted_row)
                    #traits_ui.total_points += traits_ui.change_total_points(traits_ui.total_points, traits_ui.listed_attributes[traits_ui.highlighted_row].value)


            elif isinstance(action, Submit):
                if CHAR_CURRENT_SCREEN == "RACE_SCREEN":
                    #data.save_char_data(data.player_data, "race", race_ui.available_races[race_ui.highlighted_row-1].name)
                    player_symbol = race_ui.available_races[race_ui.highlighted_row-1].symbol
                    data.player_data["race"] = race_ui.available_races[race_ui.highlighted_row-1].name
                    data.export_json_char(data.player_data, data.player_attributes, data.player_mods)
                    CHAR_CURRENT_SCREEN = switch_screen(CHAR_CURRENT_SCREEN)

                elif CHAR_CURRENT_SCREEN == "CLASS_SCREEN":
                    data.player_data["class"] = class_ui.available_classes[class_ui.highlighted_row-1].name
                    data.export_json_char(data.player_data, data.player_attributes, data.player_mods)
                    CHAR_CURRENT_SCREEN = switch_screen(CHAR_CURRENT_SCREEN)

                    #i = 0
                    current_class = class_ui.available_classes[class_ui.highlighted_row-1]
                    #for m in current_class.attributes_modifiers:
                    #    data.player_mods[i] = int(m[0][1])
                    #    i+=1
                    #dirty solution but whatever at this point x)
                    if isinstance(current_class, class_derived.Mage):
                        data.player_mods = [-2, 0, +3, -3, 0]
                    elif isinstance(current_class, class_derived.Necromancer):
                        data.player_mods = [1, 0, +3, -3, -1]
                    elif isinstance(current_class, class_derived.Cleric):
                        data.player_mods = [1, -1, -3, -1, 3]
                    elif isinstance(current_class, class_derived.Warrior):
                        data.player_mods = [2, 2, -2, 3, -2]
                    data.export_json_char(data.player_data, data.player_attributes, data.player_mods)

                elif CHAR_CURRENT_SCREEN == "TRAITS_SCREEN":
                    for a in range(len(data.player_attributes)):
                        data.player_attributes[a] = traits_ui.listed_attributes[a].value
                        print(data.player_attributes[a])
                    data.export_json_char(data.player_data, data.player_attributes, data.player_mods)

                #if CHAR_CURRENT_SCREEN == "BIO_SCREEN":
                #    #data.save_char_data(data.player_data, "gender", bio_ui.builtin_genders[(screen_width//5)//bio_ui.highlighted_gender_column])
                #    #TOFIX: fix all this shit i can't figure it out might a well scrap the bio section for now
                #    data.player_data["bio"]["gender"] = bio_ui.builtin_genders[(screen_width//5)*(bio_ui.highlighted_gender_column//5)]
                #    data.export_json_char(data.player_data)


            elif isinstance(action, Pass):
                if CHAR_CURRENT_SCREEN == "BIO_SCREEN":
                    CHAR_CURRENT_SCREEN = switch_screen(CHAR_CURRENT_SCREEN)

            elif isinstance(current_event, event.Quit):
                raise SystemExit()