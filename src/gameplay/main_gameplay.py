#coding:utf-8

"""
notes
    ? docs
        ? this file serves as a template to get a basic window up
        ? and running (tailored to the needs) of the Arithmancy project

        ? this file was written after the file found on the the tcod library documentation's website
        ? ( https://python-tcod.readthedocs.io/en/latest/tcod/getting-started.html )
"""


#type hinting
from typing import List, Dict



#modules
from tcod import *

import private.cli_args.arg_parsing as arg_parsing

import assets.color_tokens as color_tokens

#modules init





#classes
class Element:
    """Game element class.\n
    Serves as the highest base class for all custom game elements."""

    def __init__(self, name:str, tile:str) -> None:
        self.name:str = name
        self.tile:str = tile

    def __repr__(self) -> str:
        return f"{self.tile} : {self.name}"



class Entity(Element):
    """Entities elements class.\n
    Inherits from the `Element` base class.\n
    Serves as a base class for entities (`Entity` class objects)."""

    def __init__(self, name:str, tile:str, adjectives_list:List[str], hp:int, max_hp:int) -> None:
        super().__init__(name, tile)
        self.adjectives:List[str] = adjectives_list
        self.hp:int = hp
        self.max_hp:int = max_hp

    def move(self):
        raise NotImplementedError()

    def attack(self):
        raise NotImplementedError()



class Player(Entity):
    """Player character object class.\n
    Inherits from the `Entity` base class.\n
    Inherits from interfaces (base classes) for its player-selected character class."""

    def __init__(self, name: str, tile: str, adjectives_list: List[str], hp: int, max_hp: int) -> None:
        super().__init__(name, tile, adjectives_list, hp, max_hp)

        self.race:str = "SAMPLE_RACE"
        self.name = "SAMPLE_NAME"               #TODO: set name to randomly-assigned one
        self.gender = None                      #TODO: implement gender once text input has been fixed

        self.char_class:str = "SAMPLE_CLASS"    #TODO: set class to selected one
        self.traits:Dict[str, int] = {
            "CON":10,
            "DEX":10,
            "INT":10,
            "STR":10,
            "WIS":10,
        }


        self.adjectives = [
            "ambitious",
            "bold", "brave",
            "daring", "desperate",
            "famous", "fortunate",
            "great",
            "intrepid",
            "lawless",
            "reckless",
            "successful",
            "unfortunate", "unscrupulous",
            "wild"
        ]

        self.level:int = 1; #§ default value | TODO: allow to be set to 0 with debug


    def move(self):
        raise NotImplementedError()


    def level_up(self):
        raise NotImplementedError()





#functions
def create_player_object(player_object:Player, player_data:dict):
    """Creates the `player_object` instance used during gameplay using preemptively saved `player_data`.\n
    Returns ??? (`???`)."""
    pass





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