#coding:utf-8

#type checking
from typing import Optional



#modules
import tcod

from .event_types import *



#classes
#main menu
class MainMenuEventHandler(tcod.event.EventDispatch):
    def ev_quit(self, event:tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action:Optional[Action] = None
        key = event.sym

        if key == tcod.event.K_UP:
            action = MainMenuOptionAction(-1)
        elif key == tcod.event.K_DOWN:
            action = MainMenuOptionAction(+1)

        elif key == tcod.event.K_RETURN:
            action = MainMenuOptionSelection()

        return action

"""? this is the previous main menu event handling code, i keep it here just in case... too scared too delete...
if isinstance(current_event, event.KeyDown) and current_event.sym == event.KeySym.DOWN:
    MAIN_MENU_OPTIONS_SELECTED_ROW += 1
    if MAIN_MENU_OPTIONS_SELECTED_ROW > len(MAIN_MENU_OPTIONS.options):
        MAIN_MENU_OPTIONS_SELECTED_ROW = len(MAIN_MENU_OPTIONS.options)
    print(f"Current option row: {MAIN_MENU_OPTIONS_SELECTED_ROW}") #? debug

elif isinstance(current_event, event.KeyDown) and current_event.sym == event.KeySym.UP:
    MAIN_MENU_OPTIONS_SELECTED_ROW -= 1
    if MAIN_MENU_OPTIONS_SELECTED_ROW < 1:
        MAIN_MENU_OPTIONS_SELECTED_ROW = 1
    print(f"Current option row: {MAIN_MENU_OPTIONS_SELECTED_ROW}") #? debug

elif isinstance(current_event, event.KeyDown) and current_event.sym == event.KeySym.RETURN:
    print(f"Selected option: \"{MAIN_MENU_OPTIONS.options[MAIN_MENU_OPTIONS_SELECTED_ROW - 1]}\"")
"""

#options screen
class OptionsScreenEventHandler(tcod.event.EventDispatch):
    def ev_quit(self, event:tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action:Optional[Action] = None
        key = event.sym

        if key == tcod.event.K_ESCAPE:
            action = OptionsScreenGoBack()

        return action

#about screen
class AboutScreenEventHandler(tcod.event.EventDispatch):
    def ev_quit(self, event:tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action:Optional[Action] = None
        key = event.sym

        if key == tcod.event.K_ESCAPE:
            action = AboutScreenGoBack()

        return action



#character creation
class CharacterCreatorEventHandler(tcod.event.EventDispatch):
    def ev_quit(self, event:tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    #def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
    #    action:Optional[Action] = None
    #    key = event.sym

    #    if key == tcod.event.K_ESCAPE:
    #        action = AboutScreenGoBack()

    #    return action