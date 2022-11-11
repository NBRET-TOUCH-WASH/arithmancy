#coding:utf-8

class OptionRowChange:
    """Represents the user going up or down different rows of options."""
    def __init__(self, row_change:int) -> None:
        self.row_change:int = row_change



class Submit:
    """Represents the user selecting a certain option, entering a string, etc."""
    def __init__(self) -> None:
        return None