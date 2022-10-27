#coding:utf-8

#typechecking
from tcod import Console

class MainMenu:
    """Class used for Arithmancy's main menu.\n
    Contains every element specificated."""

    def __init__(self, header_path:str|None=None, options_list:list|None=["Quit"], condensed_credits:dict|None=None, version_tag:str|None="vX.Y.Z") -> None:
        self.header = header_path
        self.options_list = options_list
        self.condensed_credits = condensed_credits
        self.version_tag = version_tag

    def __repr__(self) -> str:
        return f"Main menu for \"Arithmancy\" {self.version_tag}"

    def print_menu(self, target_console:Console) -> None:
        pass