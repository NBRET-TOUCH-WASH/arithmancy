#coding:utf-8



class Player:
    """An example player character class.\n
    Does not represent the final player class."""

    def __init__(self, name:str, hp:int, mp:int, start_level:int, states:dict, title:str|None = None) -> None:
        #e.g. "High Lord" + "Wolnir", None + "Soul of Cinder"
        self.name = name
        self.title = title
        self.full_name = title + name

        self.hp = hp
        self.mp = mp
        self.level = start_level

        self.states = {
            "ablaze":states["ablaze"],
            "asleep":states["asleep"],
            "blind":states["blind"],
            "confused":states["confused"],
            "hexed":states["hexed"],
            "poisoned":states["poisoned"]
        }

    def __repr__(self) -> str:
        return f"{self.name} ; LVL {self.level}\n{self.hp} HP | {self.mp} MP"

    def describe_movement(self) -> str:
        return f"{self.name} moves about aimlessly..."