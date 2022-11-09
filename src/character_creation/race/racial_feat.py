#coding:utf-8

#type hinting
from assets import color_tokens



#base attributes class
class RacialFeat:
    """Represents a racial feat in the character creation segment. \
    Is not used in the main gameplay section.\n
    Serves as a race's attribute's class for the character creation segment."""

    feats_types:dict = {
        "DEBUFF":color_tokens.MAROON.rgb,
        "NEUTRAL":color_tokens.EGGPLANT.rgb,
        "BUFF":color_tokens.SPRING_GREEN.rgb
    }

    def __init__(self) -> None:
        self.name:str = ""
        self.info:str = ""

        self.type:str = "NEUTRAL"


class NoRacialFeat(RacialFeat):
    """Represents the lack of racial feats. \
    Is not used in the main gameplay section.\n
    Serves as a race's attribute's class for the character creation segment."""
    def __init__(self) -> None:
        super().__init__()
        self.name = "No notable racial feats."



#derived attributes class
#buffs
class BiologicalImmortality(RacialFeat):
    """Represents a racial feat in the character creation segment. \
    Is not used in the main gameplay section.\n
    Serves as a race's attribute's class for the character creation segment.\n
    This feats makes individuals of the affected race immune to cecity (blindness)."""
    def __init__(self) -> None:
        self.name = "Biological Immortality"
        self.info = "Character will not die of old age and only to violence and disease instead."

        self.type = "BUFF"


class CecityImmunity(RacialFeat):
    """Represents a racial feat in the character creation segment. \
    Is not used in the main gameplay section.\n
    Serves as a race's attribute's class for the character creation segment.\n
    This feats makes individuals of the affected race immune to cecity (blindness)."""
    def __init__(self) -> None:
        self.name = "Cecity Immunity"
        self.info = "Character cannot be blinded by magical means.\nPhysical injuries and wounds to the eyes can however impact the character's sense of sight."

        self.type = "BUFF"


class Cuteness(RacialFeat):
    """Represents a racial feat in the character creation segment. \
    Is not used in the main gameplay section.\n
    Serves as a race's attribute's class for the character creation segment.\n
    This feats makes individuals of the affected race cute."""
    def __init__(self) -> None:
        self.name = "Cuteness"
        self.info = "Character is very cute."

        self.type = "BUFF"


#debuffs
class Alcoholism(RacialFeat):
    """Represents a racial feat in the character creation segment. \
    Is not used in the main gameplay section.\n
    Serves as a race's attribute's class for the character creation segment.\n
    This feats makes individuals of the affected race alcoholic."""
    def __init__(self) -> None:
        self.name = "Alcoholism"
        self.info = "Character requires alcoholic beverages to remain sane, safe and sound."

        self.type = "DEBUFF"


class ProtectorOfNature(RacialFeat):
    """Represents a racial feat in the character creation segment. \
    Is not used in the main gameplay section.\n
    Serves as a race's attribute's class for the character creation segment.\n
    This feats makes individuals of the affected race dedicated to protect nature \
    (thus not using wooden items, etc)."""
    def __init__(self) -> None:
        self.name = "Protector of Nature"
        self.info = "Character is a devoted protector of nature due to their supernatural connection with it.\nAs such, they cannot use wooden items."

        self.type = "DEBUFF"