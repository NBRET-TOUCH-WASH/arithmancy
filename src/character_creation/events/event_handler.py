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


        elif key == tcod.event.K_LEFT:
            action = OptionColumnChange(-(Action.screen_width//5))
        elif key == tcod.event.K_RIGHT:
            action = OptionColumnChange(+(Action.screen_width//5))


        elif key == tcod.event.K_RETURN:
            action = Submit()
        elif key == tcod.event.K_SPACE:
            action = Pass()


        elif key == tcod.event.K_EQUALS or key == tcod.event.K_KP_PLUS:
            action = Increment()
        #! the `K_6` key is the '-' (minus) key
        elif key == tcod.event.K_6 or key == tcod.event.K_KP_MINUS:
            action = Decrement()

        return action