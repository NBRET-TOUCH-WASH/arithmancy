#coding:utf-8

#type checking
from typing import Optional



#modules
import tcod

from .event_types import *



#classes
class Action:
    pass


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

        return action