#coding:utf-8

#modules
from tcod import *

from .events import *



#functions
def main_char_creation(context:context.Context, console:Console, screen_width:int, screen_height:int):
    """"""

    char_creator_event_handler = CharacterCreatorEventHandler()

    while True:
        console.print(0,0, "bruh", (255,255,255),(0,0,0))

        for current_event in event.wait():
            context.convert_event(current_event)
            print(current_event)

            action = char_creator_event_handler.dispatch(current_event)
            print(current_event)


            if action is None:
                continue

            elif isinstance(current_event, event.Quit):
                raise SystemExit()