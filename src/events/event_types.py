#coding:utf-8

#modules

#classes
class Action:
    pass

class GoBack:
    pass


#class QuitAction(Action):
#    pass

#main menu
class MainMenuOptionAction(Action):
    def __init__(self, row_change:int) -> None:
        super().__init__()
        self.row_change = row_change

class MainMenuOptionSelection(Action):
    def __init__(self) -> None:
        super().__init__()
        #self.option_row = option_row

#options screen
class OptionsScreenGoBack(GoBack):
    def __init__(self) -> None:
        super().__init__()

#about screen
class AboutScreenGoBack(GoBack):
    def __init__(self) -> None:
        super().__init__()