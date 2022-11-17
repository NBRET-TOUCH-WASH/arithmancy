#coding:utf-8

#classes
class Action:
    screen_width:int = 155
    screen_height:int = 55



#TODO: make this work later, for now we'll use a randomly-selected name
#class TextInput(Action):
#    """Represents text being input by the user."""
#    def __init__(self, char:str) -> None:
#        self.char:str = char



class OptionRowChange(Action):
    """Represents the user going up or down different rows of options."""
    def __init__(self, row_change:int) -> None:
        self.row_change:int = row_change

class OptionColumnChange(Action):
    """Represents the user going up or down different rows of options."""
    def __init__(self, column_change:int) -> None:
        self.column_change:int = column_change



class Submit(Action):
    """Represents the user selecting a certain option, entering a string, etc."""
    def __init__(self) -> None:
        return None