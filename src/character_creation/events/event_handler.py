#coding:utf-8

#type checking
from typing import Optional



#modules
import tcod

from .event_types import *

#text input
#TODO: make this work later, for now we'll use a randomly-selected name
#class TextInputHandler(tcod.event.EventDispatch):
#    #alphabet = {
#    #    tcod.event.K_a:'a',
#    #    tcod.event.K_b:'b',
#    #    tcod.event.K_c:'c',
#    #}


#    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
#        pass

#    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
#        action:Optional[Action] = None
#        key = event.sym

#        if key == tcod.event.K_UP:
#            pass

#        return action


#character creation
class CharacterCreatorEventHandler(tcod.event.EventDispatch):
    def ev_quit(self, event:tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action:Optional[Action] = None
        key = event.sym

        if key == tcod.event.K_UP:
            action = OptionRowChange(-1)
        elif key == tcod.event.K_DOWN:
            action = OptionRowChange(+1)

        if key == tcod.event.K_LEFT:
            action = OptionColumnChange(-(Action.screen_width//5))
        if key == tcod.event.K_RIGHT:
            action = OptionColumnChange(+(Action.screen_width//5))

        elif key == tcod.event.K_RETURN:
            action = Submit()

        return action